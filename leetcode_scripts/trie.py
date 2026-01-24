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
    
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
    
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

# Tests
def test_trie():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True, "Test 1 failed"
    assert trie.search("app") == False, "Test 2 failed"
    assert trie.startsWith("app") == True, "Test 3 failed"
    trie.insert("app")
    assert trie.search("app") == True, "Test 4 failed"
    assert trie.startsWith("appl") == True, "Test 5 failed"
    assert trie.startsWith("banana") == False, "Test 6 failed"
    trie.insert("banana")
    assert trie.search("banana") == True, "Test 7 failed"
    assert trie.startsWith("ban") == True, "Test 8 failed"
    assert trie.search("ban") == False, "Test 9 failed"
    print("All tests passed.")

if __name__ == "__main__":
    test_trie()
