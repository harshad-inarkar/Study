class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0] or not words:
            return []

        result = []
        trie = Trie()
        # build trie
        for w in words:
            trie.insert(w)
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r,c,node, path):


            ch = board[r][c]

            if ch not in node.children:
                return
            
            nxtnode = node.children[ch]
            newpath = path+ch

            if nxtnode.is_end:
                result.append(newpath)
                nxtnode.is_end = False

                # prune if this node has no more children
                if not nxtnode.children:
                    del node.children[ch]
                    return
            
            # URDL
            board[r][c] = '#'
            for dr, dc in (-1,0),(0,1), (1,0), (0,-1):
                nr, nc = r+dr, c+dc

                if  0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr,nc, nxtnode, newpath)
                
            board[r][c] = ch


        for i in range(rows):
            for j in range(cols):
                dfs(i,j,trie.root, '')

        return result

# Example usage and test
def test_findWords():
    sol = Solution()
    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words = ["oath","pea","eat","rain"]
    assert sorted(sol.findWords(board, words)) == sorted(["eat","oath"]), "Test 1 failed"

    board2 = [["a","b"],["c","d"]]
    words2 = ["abcb"]
    assert sol.findWords(board2, words2) == [], "Test 2 failed"

    board3 = [["a"]]
    words3 = ["a"]
    assert sol.findWords(board3, words3) == ["a"], "Test 3 failed"

    print("All tests passed.")

if __name__ == "__main__":
    test_findWords()
