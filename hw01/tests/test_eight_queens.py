import pytest
from src.eight_queens import EightQueensSolver

def test_n_queens_solutions():
    # 测试N=4，应有2个解
    solver4 = EightQueensSolver(4)
    solutions4 = solver4.get_solutions()
    assert len(solutions4) == 2

    # 测试N=8，应有92个解
    solver8 = EightQueensSolver(8)
    solutions8 = solver8.get_solutions()
    assert len(solutions8) == 92

if __name__ == "__main__":
    pytest.main([__file__])