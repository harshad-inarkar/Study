def isSubsequence(s: str, t: str) -> bool:
    """
    Returns True if s is a subsequence of t, False otherwise.
    """
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

# Test cases
def test_isSubsequence():
    assert isSubsequence("abc", "ahbgdc") == True
    assert isSubsequence("axc", "ahbgdc") == False
    assert isSubsequence("", "ahbgdc") == True
    assert isSubsequence("abc", "") == False
    assert isSubsequence("", "") == True
    assert isSubsequence("a", "a") == True
    assert isSubsequence("b", "c") == False
    print("All test cases passed!")

test_isSubsequence()
