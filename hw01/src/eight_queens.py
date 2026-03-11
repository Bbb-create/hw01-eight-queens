class EightQueensSolver:
    def __init__(self, n: int = 8):
        self.n = n
        self.solutions = []

    def is_safe(self, board: list, row: int, col: int) -> bool:
        # 检查列
        for i in range(row):
            if board[i][col] == 1:
                return False
        # 检查左上对角线
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 1:
                return False
        # 检查右上对角线
        for i, j in zip(range(row-1, -1, -1), range(col+1, self.n)):
            if board[i][j] == 1:
                return False
        return True

    def solve(self, board: list, row: int) -> None:
        if row == self.n:
            solution = []
            for r in board:
                solution.append(r.copy())
            self.solutions.append(solution)
            return
        for col in range(self.n):
            if self.is_safe(board, row, col):
                board[row][col] = 1
                self.solve(board, row + 1)
                board[row][col] = 0

    def get_solutions(self) -> list:
        board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.solve(board, 0)
        return self.solutions

    def print_solutions(self) -> None:
        for idx, sol in enumerate(self.solutions, 1):
            print(f"Solution {idx}:")
            for row in sol:
                print(" ".join("Q" if cell == 1 else "." for cell in row))
            print()