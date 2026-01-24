def ladderLength(beginWord, endWord, wordList):
    """
    Returns the length of shortest transformation sequence from beginWord to endWord.
    Each transformation must change exactly one letter and be in wordList.
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    from collections import deque

    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque()
    queue.append((beginWord, 1))
    visited = set()
    visited.add(beginWord)

    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == word[i]:
                    continue
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordSet and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))
    return 0

# Tests
def test_ladderLength():
    # Test 1: Example from Leetcode
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    assert ladderLength(beginWord, endWord, wordList) == 5, "Test 1 failed"

    # Test 2: No possible transformation
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    assert ladderLength(beginWord, endWord, wordList) == 0, "Test 2 failed"

    # Test 3: Begin equals end
    beginWord = "a"
    endWord = "a"
    wordList = ["a"]
    assert ladderLength(beginWord, endWord, wordList) == 1, "Test 3 failed"

    # Test 4: One letter difference
    beginWord = "a"
    endWord = "c"
    wordList = ["a", "b", "c"]
    assert ladderLength(beginWord, endWord, wordList) == 2, "Test 4 failed"

    # Test 5: No wordList
    beginWord = "hit"
    endWord = "cog"
    wordList = []
    assert ladderLength(beginWord, endWord, wordList) == 0, "Test 5 failed"

    # Test 6: Case with cycles
    beginWord = "red"
    endWord = "tax"
    wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
    assert ladderLength(beginWord, endWord, wordList) == 4, "Test 6 failed"

    print("All tests passed.")

if __name__ == "__main__":
    test_ladderLength()
