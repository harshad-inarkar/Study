from collections import deque

def solve(board):
    """
    Modifies the board in-place. Captures all regions surrounded by 'X' using BFS.
    A region is captured if it is surrounded by 'X' on all sides.
    """
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        board[r][c] = 'E'
        while queue:
            cr, cc = queue.popleft()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    board[nr][nc] = 'E'
                    queue.append((nr, nc))

    # Mark all 'O's on the border and their connected 'O's as escaped using BFS
    for r in range(rows):
        if board[r][0] == 'O':
            bfs(r, 0)
        if board[r][cols-1] == 'O':
            bfs(r, cols-1)
    for c in range(cols):
        if board[0][c] == 'O':
            bfs(0, c)
        if board[rows-1][c] == 'O':
            bfs(rows-1, c)

    # Flip all remaining 'O's to 'X', and 'E's back to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'E':
                board[r][c] = 'O'

# Tests
def test_solve():
    # Test 1: Example case
    board1 = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    expected1 = [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]
    ]
    solve(board1)
    assert board1 == expected1

    # Test 2: All 'O's
    board2 = [
        ["O","O"],
        ["O","O"]
    ]
    expected2 = [
        ["O","O"],
        ["O","O"]
    ]
    solve(board2)
    assert board2 == expected2

    # Test 3: Surrounded single 'O'
    board3 = [
        ["X","X","X"],
        ["X","O","X"],
        ["X","X","X"]
    ]
    expected3 = [
        ["X","X","X"],
        ["X","X","X"],
        ["X","X","X"]
    ]
    solve(board3)
    assert board3 == expected3

    # Test 4: No 'O's
    board4 = [
        ["X","X"],
        ["X","X"]
    ]
    expected4 = [
        ["X","X"],
        ["X","X"]
    ]
    solve(board4)
    assert board4 == expected4

    # Test 5: Empty board
    board5 = []
    expected5 = []
    solve(board5)
    assert board5 == expected5

    # Test 6: Single row
    board6 = [["O","X","O","O","X"]]
    expected6 = [["O","X","O","O","X"]]
    solve(board6)
    assert board6 == expected6

    # Test 7: Single column
    board7 = [["O"],["X"],["O"],["O"],["X"]]
    expected7 = [["O"],["X"],["O"],["O"],["X"]]
    solve(board7)
    assert board7 == expected7

    print("All tests passed.")

if __name__ == "__main__":
    test_solve()

