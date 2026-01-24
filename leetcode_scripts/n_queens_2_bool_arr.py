def total_n_queens(n):
    """
    Returns the number of distinct solutions to the n-queens puzzle.
    """
    count = 0
    cols, diag1, diag2 = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
    
    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return

        for col in range(n):
            d1 = row-col+n-1
            d2 = row+col
            if cols[col] or diag1[d1] or diag2[d2]:
                continue

            cols[col] = diag1[d1] = diag2[d2] = True
            backtrack(row + 1)
            cols[col] = diag1[d1] = diag2[d2] = False

    backtrack(0)
    return count

# Tests
def test_total_n_queens():
    assert total_n_queens(1) == 1, "Failed on n=1"
    assert total_n_queens(2) == 0, "Failed on n=2"
    assert total_n_queens(3) == 0, "Failed on n=3"
    assert total_n_queens(4) == 2, "Failed on n=4"
    assert total_n_queens(5) == 10, "Failed on n=5"
    assert total_n_queens(6) == 4, "Failed on n=6"
    assert total_n_queens(7) == 40, "Failed on n=7"
    assert total_n_queens(8) == 92, "Failed on n=8"
    print("All tests passed.")

test_total_n_queens()
