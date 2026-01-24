def isAnagram(s: str, t: str) -> bool:
    """
    Returns True if t is an anagram of s, False otherwise.
    """
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        if c not in count or count[c] == 0:
            return False
        count[c] -= 1
    return True

# Tests
def test_isAnagram():
    assert isAnagram("anagram", "nagaram") == True
    assert isAnagram("rat", "car") == False
    assert isAnagram("", "") == True
    assert isAnagram("a", "a") == True
    assert isAnagram("ab", "ba") == True
    assert isAnagram("abc", "cba") == True
    assert isAnagram("aabbcc", "abcabc") == True
    assert isAnagram("aabbcc", "aabbc") == False
    assert isAnagram("aabbcc", "aabbccd") == False
    print("All tests passed!")

test_isAnagram()
