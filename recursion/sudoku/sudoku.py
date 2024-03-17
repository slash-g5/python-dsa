class Sudoku:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def change_board(self, board):
        self.board = board

    def readFile(self, file):
        f = open(file, "r")
        i = -1
        for line in f:
            i += 1
            self.board[i] = list(map(int, line.split()))

    def print_sudoku(self):
        for i in range(9):
            print("|", end=" ")
            for j in range(9):
                print(self.board[i][j], end=" |")
            print()

    def check_complete_sudoku(self):
        # check all row
        for i in range(9):
            not_visited = {value for value in range(1, 10)}
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
                if self.board[i][j] not in not_visited:
                    return False
                not_visited.remove(self.board[i][j])
            if not_visited:
                return False

        # check all col
        for j in range(9):
            not_visited = {value for value in range(1, 10)}
            for i in range(9):
                if self.board[i][j] == 0:
                    return False
                if self.board[i][j] not in not_visited:
                    return False
                not_visited.remove(self.board[i][j])
            if not_visited:
                return False

        # check all boxes
        # boxes = (i,j) => i,j in {0,1,2} box from (3*i to 3i+2, 3*j to 3*j+2)
        for i in range(3):
            for j in range(3):
                if not self.check_box(i, j):
                    return False

        # All rows, cols and boxes checked, returning true
        return True

    def check_box(self, i, j):
        not_visited = {value for value in range(1, 10)}
        for x in range(3 * i, 3 * i + 3):
            for y in range(3 * j, 3 * j + 3):
                if self.board[x][y] == 0:
                    return False
                if self.board[x][y] not in not_visited:
                    return False
                not_visited.remove(self.board[x][y])
        if not_visited:
            return False
        return True

    def is_possible_to_add(self, i, j, value):
        # check row
        for y in range(9):
            if self.board[i][y] == value:
                return False
        # check col
        for x in range(9):
            if self.board[x][j] == value:
                return False
        # check box
        box_x = i // 3
        box_y = j // 3
        for i1 in range(box_x * 3, box_x * 3 + 3):
            for j1 in range(box_y * 3, box_y * 3 + 3):
                if self.board[i1][j1] == value:
                    return False
        return True


def Test():
    sudoku = Sudoku()
    sudoku.readFile("input.txt")
    sudoku.print_sudoku()
    print(sudoku.check_complete_sudoku())
    print(sudoku.is_possible_to_add(2, 5, 7))


if __name__ == "__main__":
    Test()
