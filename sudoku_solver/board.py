class SudokuBoard(object):
    def __init__(self, board: list[list[int]]):
        self.board = board
        self.numberBoard = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(9)] for j in range(9)]
        # self.init_board()

    def check_square(self, row, col, num):
        row = row - row % 3
        col = col - col % 3
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if self.board[i][j] == num:
                    for k in range(row, row + 3):
                        for l in range(col, col + 3):
                            if self.numberBoard[k][l].count(num) == 1:
                                self.numberBoard[k][l].remove(num)
        return True

    def check_row(self, row, num):
        for nums in self.numberBoard[row]:
            if nums.count(num) == 1:
                nums.remove(num)
        return True

    def check_col(self, col, num):
        for i in range(9):
            if self.numberBoard[i][col].count(num) == 1:
                self.numberBoard[i][col].remove(num)
        return True

    def update_board(self):
        for i in range(9):
            for j in range(9):
                if len(self.numberBoard[i][j]) == 1:
                    self.board[i][j] = self.numberBoard[i][j][0]

    def check_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        return True

    def solve(self):
        while True:
            for i in range(9):
                for j in range(9):
                    if self.board[i][j] != 0:
                        # print(self.numberBoard)
                        # input("next")
                        self.numberBoard[i][j] = [self.board[i][j]]
                        self.check_col(j, self.board[i][j])
                        self.check_row(i, self.board[i][j])
                        self.check_square(i, j, self.board[i][j])
            print(self.numberBoard)
            self.update_board()
            self.print_board()
            if self.check_board():
                break

    def print_board(self):
        print(10 * "\n")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("---------------------------------------")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                print(f" {self.board[i][j]} ", end=" ")
            print("")
