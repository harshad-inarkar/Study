class WordDictionaryNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = WordDictionaryNode()
    
    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionaryNode()
            node = node.children[ch]
        node.is_end = True
    
    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            else:
                if ch in node.children:
                    return dfs(node.children[ch], i+1)
                else:
                    return False
        return dfs(self.root, 0)

# Tests
def test_WordDictionary():
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") == False, "Test 1 failed"
    assert wd.search("bad") == True, "Test 2 failed"
    assert wd.search(".ad") == True, "Test 3 failed"
    assert wd.search("b..") == True, "Test 4 failed"
    assert wd.search("..d") == True, "Test 5 failed"
    assert wd.search("b.d") == True, "Test 6 failed"
    assert wd.search("ba") == False, "Test 7 failed"
    wd.addWord("a")
    assert wd.search("a") == True, "Test 8 failed"
    assert wd.search(".") == True, "Test 9 failed"
    assert wd.search("..") == False, "Test 10 failed"
    print("All tests passed.")

if __name__ == "__main__":
    test_WordDictionary()
