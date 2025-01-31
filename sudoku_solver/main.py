from board import SudokuBoard

BOARD = [
    [0, 0, 0, 8, 0, 6, 0, 0, 2],
    [9, 4, 0, 1, 0, 5, 7, 3, 8],
    [2, 1, 8, 7, 0, 9, 4, 6, 9],
    [0, 8, 5, 0, 9, 0, 0, 7, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 3],
    [4, 6, 0, 2, 7, 0, 0, 0, 0],
    [0, 2, 4, 0, 0, 0, 3, 0, 9],
    [0, 0, 0, 9, 0, 0, 5, 4, 0],
    [5, 0, 0, 0, 8, 0, 0, 0, 0]
]

qwdqwd = [
    [[3, 7], [3, 5, 7], [3, 7], [], [4], [], [], [5], []], [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []], [[1, 3], [], [], [3, 6], [], [1, 3], [2, 6], [], [1, 4, 6]],
    [[1, 7], [7, 9], [1, 2, 7, 9], [], [1, 5, 6], [1, 8], [2, 6, 8, 9], [1, 2, 5, 8, 9], []],
    [[], [], [1, 3, 9], [], [], [1, 3, 8], [8, 9], [1, 5, 8, 9], [1, 5]],
    [[1, 6, 7, 8], [], [], [5, 6], [1, 5, 6], [1, 7], [], [1, 8], []],
    [[1, 3, 6, 7, 8], [3, 7], [1, 3, 7], [], [1, 6], [1, 2, 3, 7], [], [], [1, 6, 7]],
    [[], [3, 7, 9], [1, 3, 7, 9], [3, 6], [], [1, 2, 3, 4, 7], [2, 6], [1, 2], [1, 6, 7]]
]


def main():
    sudoku_board = SudokuBoard(BOARD)
    sudoku_board.solve()
    sudoku_board.print_board()


if __name__ == "__main__":
    main()
