import unittest
import tempfile
import src.day6 as subject

class testGrid(unittest.TestCase):
    def test_short_path(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as input_file:
            input_file.write("""
                .#...
                ^.#..
                ...#.
            """)
        grid = subject.Grid(input_file.name)
        self.assertEqual(grid.get_touched_cells(), 1)
        grid.walk()
        self.assertEqual(grid.get_touched_cells(), 2)

