def exist(board, word):
    if not board or not board[0] or not word:
        return False
    
    rows, cols, n = len(board), len(board[0]), len(word)
    
    def dfs(r,c,idx):

        if  r < 0 or r >=rows or c < 0 or c >=cols or board[r][c] != word[idx]:
            return False
        
        if idx == n-1:
            return True
        # URDL
        
        board[r][c] = '#'
        found =  (dfs(r-1,c,idx+1) or
                    dfs(r,c+1,idx+1) or
                    dfs(r+1,c,idx+1) or 
                    dfs(r,c-1,idx+1))
        
        board[r][c] = word[idx]

        return found


    count = {}
    for c in word:
        count[c] = 1 + count.get(c, 0)
    
    if count[word[0]] > count[word[-1]]:
        word = word[::-1]


    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and dfs(i,j,0):
                return True
    
    return False


# Tests
def test_exist():
    board1 = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert exist([row[:] for row in board1], "ABCCED") == True
    assert exist([row[:] for row in board1], "SEE") == True
    assert exist([row[:] for row in board1], "ABCB") == False

    board2 = [
        ['a','b'],
        ['c','d']
    ]
    assert exist([row[:] for row in board2], "abcd") == False
    assert exist([row[:] for row in board2], "ab") == True
    assert exist([row[:] for row in board2], "acdb") == True

    board3 = [
        ['A']
    ]
    assert exist([row[:] for row in board3], "A") == True
    assert exist([row[:] for row in board3], "B") == False

    print("All tests passed.")

if __name__ == "__main__":
    test_exist()
