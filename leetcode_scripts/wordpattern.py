def wordPattern(pattern: str, s: str) -> bool:
    """
    Determines if a string s follows the same pattern as given in pattern.
    Each character in pattern maps to a word in s bijectively.
    """
    words = s.split()
    if len(pattern) != len(words):
        return False
    char_to_word = {}
    word_to_char = {}
    for c, w in zip(pattern, words):
        if c in char_to_word:
            if char_to_word[c] != w:
                return False
        else:
            char_to_word[c] = w
        if w in word_to_char:
            if word_to_char[w] != c:
                return False
        else:
            word_to_char[w] = c
    return True

# Tests
def test_wordPattern():
    assert wordPattern("abba", "dog cat cat dog") == True
    assert wordPattern("abba", "dog cat cat fish") == False
    assert wordPattern("aaaa", "dog cat cat dog") == False
    assert wordPattern("abba", "dog dog dog dog") == False
    assert wordPattern("abc", "b c a") == True
    assert wordPattern("abc", "b b b") == False
    assert wordPattern("", "") == True
    assert wordPattern("a", "dog") == True
    assert wordPattern("a", "dog cat") == False
    assert wordPattern("ab", "dog") == False
    print("All tests passed!")

test_wordPattern()
