from sudoku import Sudoku


class Solver:
    def __init__(self, sudoku: Sudoku):
        self.sudoku = sudoku

    @staticmethod
    def get_next_index(i, j):
        if (i, j) == (8, 8):
            return -1, -1
        if j == 8:
            return i + 1, 0
        return i, j + 1

    def solve(self, i=0, j=0):

        if (i, j) == (-1, -1):
            return True, self.sudoku.board

        if self.sudoku.board[i][j] != 0:
            return self.solve(self.get_next_index(i, j)[0], self.get_next_index(i, j)[1])

        for number in range(1, 10):
            if not self.sudoku.is_possible_to_add(i, j, number):
                continue
            self.sudoku.board[i][j] = number
            next_index_solve = self.solve(self.get_next_index(i, j)[0], self.get_next_index(i, j)[1])
            if next_index_solve[0]:
                return next_index_solve
            self.sudoku.board[i][j] = 0

        return False, []


if __name__ == "__main__":
    solver = Solver(Sudoku())
    solver.sudoku.readFile("input.txt")
    solver.sudoku.print_sudoku()
    solver.solve()
    print()
    print()
    solver.sudoku.print_sudoku()
    print(solver.sudoku.check_complete_sudoku())
