def isValidSudoku(board):
    """
    Determines if a 9x9 Sudoku board is valid.
    Only the filled cells need to be validated according to the rules:
    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.
    """
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            if val in rows[r]:
                return False
            rows[r].add(val)
            if val in cols[c]:
                return False
            cols[c].add(val)
            box_idx = (r // 3) * 3 + (c // 3)
            if val in boxes[box_idx]:
                return False
            boxes[box_idx].add(val)
    return True

# Test cases
def test_isValidSudoku():
    valid_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    invalid_row = [
        ["5","3",".",".","7",".",".",".","."],
        ["6","5",".","1","9","5",".",".","."],  # duplicate '5' in row
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    invalid_col = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        ["5",".",".",".","8",".",".","7","9"]  # duplicate '5' in column
    ]
    invalid_box = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".","3","1","9","5",".",".","."],  # duplicate '3' in top-left box
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    empty_board = [["."]*9 for _ in range(9)]

    assert isValidSudoku(valid_board) == True
    assert isValidSudoku(invalid_row) == False
    assert isValidSudoku(invalid_col) == False
    assert isValidSudoku(invalid_box) == False
    assert isValidSudoku(empty_board) == True
    print("All test cases passed!")

test_isValidSudoku()
