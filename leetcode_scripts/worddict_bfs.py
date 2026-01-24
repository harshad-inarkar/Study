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
            node = node.children.setdefault(ch,WordDictionaryNode())            
        node.is_end = True
    
    def search(self, word):
        from collections import deque
        queue = deque()
        queue.append((self.root, 0))
        while queue:
            node, i = queue.popleft()
            if i == len(word):
                if node.is_end:
                    return True
                continue
            ch = word[i]
            if ch == '.':
                for child in node.children.values():
                    queue.append((child, i+1))
            else:
                if ch in node.children:
                    queue.append((node.children[ch], i+1))
        return False

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

