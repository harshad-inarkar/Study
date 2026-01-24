# The code below was missing a function definition for solve_n_queens and had indentation issues.
# The backtrack(0) and return result lines were inside the backtrack function, which is incorrect.
# The correct structure is to define backtrack inside solve_n_queens, call backtrack(0), and then return result.

def solve_n_queens(n):
    result = []
    state = [-1] * n
    tmp = ['.'] * n

    colset, diag1, diag2 = set(), set(), set()

    def backtrack(row):
        if row == n:
            brd = []
            for c in state:
                tmp[c] = 'Q'
                brd.append(''.join(tmp))
                tmp[c] = '.'
            result.append(brd)
            return

        for col in range(n):
            # not safe
            if col in colset or (row-col) in diag1 or (row+col) in diag2:
                continue

            # safe place queen
            state[row] = col
            colset.add(col)
            diag1.add(row-col)
            diag2.add(row+col)

            backtrack(row+1)

            # backtrack
            colset.remove(col)
            diag1.remove(row-col)
            diag2.remove(row+col)

    backtrack(0)
    return result



# Simple tests
def test_n_queens():
    # Test n = 1
    res = solve_n_queens(1)
    assert res == [['Q']], f"Failed for n=1: {res}"

    # Test n = 4
    res = solve_n_queens(4)
    expected = [
        [
            ".Q..",
            "...Q",
            "Q...",
            "..Q."
        ],
        [
            "..Q.",
            "Q...",
            "...Q",
            ".Q.."
        ]
    ]
    assert sorted(res) == sorted(expected), f"Failed for n=4: {res}"

    # Test n = 2 and n = 3 (no solutions)
    assert solve_n_queens(2) == [], "Failed for n=2"
    assert solve_n_queens(3) == [], "Failed for n=3"

    print("All tests passed.")

if __name__ == "__main__":
    test_n_queens()
