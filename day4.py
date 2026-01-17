import sys

def main():
    with open(sys.argv[1]) as inputfile:
        strings = [ line.strip() for line in inputfile ]

    print(f"Instances of 'XMAS' in the input data: {count_XMAS_block(strings)}")
    print(f"X-MAS detected in the input data:      {X_MAS_detection(strings)}")

def count_XMAS_block(strings: list[str]) -> int:
    """
    :param strings: Assume a square block of strings
    :return: The count of "XMAS" and "SAMX" in rows, columns, and diagonals
    """
    N = len(strings)

    rows = strings
    columns = [
        "".join(strings[r][c] for r in range(N))
            for c in range(N)
    ]

    # example:
    # N = 3
    # d = -2, -1, 0, 1, 2
        # d = -2: [0,2]
        # d = -1: [0,1], [1,2]
        # d =  0: [0,0], [1,1], [2,2]
        # d =  1: [1,0], [2,1]
        # d =  2: [2,0]
    diagonals_topleft_to_bottomright = [
        "".join(strings[i + d][i] for i in range((abs(d) - d) // 2, N - abs(d) + (abs(d) - d) // 2))
            for d in range(-N + 1, N)
    ]

    # example:
    # N = 3
    # d = -2, -1, 0, 1, 2
        # d = -2: [0,0]
        # d = -1: [0,1], [1,0]
        # d =  0: [0,2], [1,1], [2,0]
        # d =  1: [1,2], [2,1]
        # d =  2: [2,2]
    diagonals_topright_to_bottomleft = [
        "".join(strings[i + d][N - 1 - i] for i in range((abs(d) - d) // 2, N - abs(d) + (abs(d) - d) // 2))
            for d in range(-N + 1, N)
    ]

    lines = rows + columns + diagonals_topleft_to_bottomright + diagonals_topright_to_bottomleft

    return sum(count_XMAS_line(s) for s in lines)

def count_XMAS_line(s: str) -> int:
    return s.count("XMAS") + s.count("SAMX")

def X_MAS_detection(strings: list[str]) -> int:
    """
    :param strings: Assume a square block of strings.
    :return: The count of "MAS" strings forming a cross of diagonals.
    """
    N = len(strings)

    count = 0
    for i in range(N):
        for j in range(N):
            # filter out the edges
            if i in (0, N - 1) or j in (0, N - 1):
                continue

            if strings[i][j] == "A":
                if (firstDiagonalCheck(i, j, strings) and secondDiagonalCheck(i, j, strings)):
                    count += 1

    return count

def firstDiagonalCheck(i: int, j: int, strings: list[str]) -> bool:
    return (
           (strings[i - 1][j - 1] == "M" and strings[i + 1][j + 1] == "S")
        or (strings[i - 1][j - 1] == "S" and strings[i + 1][j + 1] == "M")
    )

def secondDiagonalCheck(i: int, j: int, strings: list[str]) -> bool:
    return (
           (strings[i - 1][j + 1] == "M" and strings[i + 1][j - 1] == "S")
        or (strings[i - 1][j + 1] == "S" and strings[i + 1][j - 1] == "M")
    )

if __name__ == "__main__":
    main()
