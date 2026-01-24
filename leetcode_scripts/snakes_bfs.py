def snakesAndLadders(board):
    """
    Solves the Snakes and Ladders game using BFS.
    :type board: List[List[int]]
    :rtype: int
    """
    from collections import deque

    n = len(board)

    if n<=1:
        return 0
    
    def get_pos(s):
        # Convert square number to (row, col)
        quot, rem = divmod(s-1, n)
        row = n - 1 - quot
        if quot % 2 == 0:
            col = rem
        else:
            col = n - 1 - rem
        return row, col

    visited = set()
    queue = deque()
    queue.append((1, 0))  # (square, moves)
    visited.add(1)

    while queue:
        s, moves = queue.popleft()
        
        for i in range(1, 7):
            next_s = s + i
            if next_s > n*n:
                continue
            r, c = get_pos(next_s)
            if board[r][c] != -1:
                next_s = board[r][c]

            if next_s == n*n:
                return moves +1
            
            if next_s not in visited:
                visited.add(next_s)
                queue.append((next_s, moves+1))
    return -1

# Tests
def test_snakesAndLadders():
    # Test 1: Example from Leetcode
    board = [
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,35,-1,-1,13,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1]
    ]
    assert snakesAndLadders(board) == 4, "Test 1 failed"

    # Test 2: No snakes or ladders, 3x3
    board = [
        [-1,-1,-1],
        [-1,-1,-1],
        [-1,-1,-1]
    ]
    # Squares: 1 to 9, need to reach 9. Min moves: 2 (1->7->9)
    assert snakesAndLadders(board) == 2, "Test 2 failed"

    # Test 3: Ladder at start
    board = [
        [-1,-1,-1],
        [-1,9,-1],
        [-1,-1,-1]
    ]
    # 2 is a ladder to 9, so 1->2->9 (2 moves)
    assert snakesAndLadders(board) == 1, "Test 3 failed"

    # Test 4: Impossible to reach
    board = [
        [-1,-1,-1],
        [-1,-1,-1],
        [-1,-1,2]
    ]
    # 9 is a snake to 2, so you can never reach 9
    assert snakesAndLadders(board) == 2, "Test 4 failed"

    # Test 5: 1x1 board
    board = [[-1]]
    assert snakesAndLadders(board) == 0, "Test 5 failed"

    print("All tests passed.")

if __name__ == "__main__":
    test_snakesAndLadders()
