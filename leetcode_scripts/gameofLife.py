def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    Implements Conway's Game of Life.
    """
    if not board or not board[0]:
        return
    m, n = len(board), len(board[0])
    # Directions for 8 neighbors
    dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    # First pass: mark changes
    for i in range(m):
        for j in range(n):
            live_neighbors = 0
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n:
                    # 1 or -1 means the cell was originally alive
                    if board[ni][nj] == 1 or board[ni][nj] == -1:
                        live_neighbors += 1
            # Rule 1 or 3: live cell dies
            if board[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[i][j] = -1  # Mark as dead
            # Rule 4: dead cell becomes live
            elif board[i][j] == 0:
                if live_neighbors == 3:
                    board[i][j] = 2  # Mark as live
    # Second pass: finalize the board
    for i in range(m):
        for j in range(n):
            if board[i][j] == -1:
                board[i][j] = 0
            elif board[i][j] == 2:
                board[i][j] = 1

# Test cases
def test_gameOfLife():
    # Test 1: Blinker (oscillator)
    board = [
        [0,1,0],
        [0,1,0],
        [0,1,0]
    ]
    expected1 = [
        [0,0,0],
        [1,1,1],
        [0,0,0]
    ]
    gameOfLife(board)
    assert board == expected1, f"Test 1 failed: {board}"

    # Test 2: Block (still life)
    board2 = [
        [1,1],
        [1,1]
    ]
    expected2 = [
        [1,1],
        [1,1]
    ]
    gameOfLife(board2)
    assert board2 == expected2, f"Test 2 failed: {board2}"

    # Test 3: Empty board
    board3 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected3 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    gameOfLife(board3)
    assert board3 == expected3, f"Test 3 failed: {board3}"

    # Test 4: Single live cell (dies)
    board4 = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    expected4 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    gameOfLife(board4)
    assert board4 == expected4, f"Test 4 failed: {board4}"

    # Test 5: Glider (first step)
    board5 = [
        [0,1,0],
        [0,0,1],
        [1,1,1]
    ]
    expected5 = [
        [0,0,1],
        [1,0,1],
        [0,1,1]
    ]
    gameOfLife(board5)
    assert board5 == expected5, f"Test 5 failed: {board5}"

    print("All test cases passed!")

test_gameOfLife()
