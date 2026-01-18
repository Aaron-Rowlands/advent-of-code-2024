import re
import sys
from datetime import datetime

class Grid:
    def __init__(self, file):
        self._rows = []
        self._guard = None

        with open(file, 'r') as f:
            for line in f:
                match = re.match(r'^\s*([.#^]+)\s*$', line)
                if match:
                    row = list(match.group(1))
                    self._rows.append(row)
                    if '^' in row:
                        self._guard = Guard(row.index('^'), len(self._rows) - 1)
                        row[self._guard._x] = '|'

        self.width = len(self._rows[0])
        self.height = len(self._rows)

    def get_touched_cells(self):
        touched = 0
        for row in self._rows:
            touched += row.count('|') + row.count('-') + row.count('X')
        return touched

    def walk(self):
        while(self._guard.on_grid and not self._guard.in_a_loop):
            self._guard.walk(self)

    def is_out_of_bounds(self, x, y):
        return (
            x < 0
            or y < 0
            or y >= len(self._rows)
            or x >= len(self._rows[0])
        )

    def is_obstacle(self, x, y):
        return self._rows[y][x] == '#'

    def mark_touched(self, x, y, direction):
        if direction == 'up':
            self._rows[y][x] = '|'
        elif direction == 'right':
            self._rows[y][x] = '-'
        elif self._rows[y][x] not in ['|', '-']:
            self._rows[y][x] = 'X'

    def print(self):
        for row in self._rows:
            print(''.join(row))
        print('=' * len(self._rows[0]))

    def get_cell_state(self, x, y):
        return self._rows[y][x]

    def guard_is_in_a_loop(self):
        return self._guard.in_a_loop

    def set_obstacle(self, x, y):
        if self._guard.collides(x, y):
            raise Exception("Can't place obstacle on guard")
        else:
            self._rows[y][x] = '#'


class Guard:
    def __init__(self, x, y):
        self._x = x
        self._y = y

        self._orientation = 'up'
        self.on_grid = True
        self.in_a_loop = False

    def collides(self, x, y):
        return self._x == x and self._y == y

    def walk(self, grid: Grid):
        proposed_x = self._x
        proposed_y = self._y

        if self._orientation == 'up':
            proposed_y -= 1
        elif self._orientation == 'down':
            proposed_y += 1
        elif self._orientation == 'left':
            proposed_x -= 1
        elif self._orientation == 'right':
            proposed_x += 1

        if grid.is_out_of_bounds(proposed_x, proposed_y):
            self.on_grid = False
        elif grid.is_obstacle(proposed_x, proposed_y):
            self.turn_right()
        else:
            self._x = proposed_x
            self._y = proposed_y
            if self._orientation == 'up' and grid.get_cell_state(self._x, self._y) == '|':
                self.in_a_loop = True
            if self._orientation == 'right' and grid.get_cell_state(self._x, self._y) == '-':
                self.in_a_loop = True
            grid.mark_touched(self._x, self._y, self._orientation)

    def turn_right(self):
        orientations = ['up', 'right', 'down', 'left']
        current_index = orientations.index(self._orientation)
        self._orientation = orientations[(current_index + 1) % 4]

def main():
    input_file = sys.argv[1]
    grid = Grid(input_file)
    grid.walk()
    print("Touched cells after walk:", grid.get_touched_cells())

    loop_position_count = 0
    for y in range(grid.height):
        for x in range(grid.width):
            current_grid = Grid(input_file)
            try:
                current_grid.set_obstacle(x, y)
            except Exception:
                continue
            current_grid.walk()
            if current_grid.guard_is_in_a_loop():
                loop_position_count += 1
    print("Potential loop-causing obstacle positions:", loop_position_count)


if __name__ == "__main__":
    main()
