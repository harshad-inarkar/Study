
def isIsomorphic(s: str, t: str) -> bool:
    """
    Determines if two strings s and t are isomorphic.
    Two strings are isomorphic if the characters in s can be replaced to get t,
    with each character mapping to another character uniquely.
    """
    if len(s) != len(t):
        return False
    s2t = {}
    t2s = {}
    for cs, ct in zip(s, t):
        if cs in s2t:
            if s2t[cs] != ct:
                return False
        else:
            s2t[cs] = ct
        if ct in t2s:
            if t2s[ct] != cs:
                return False
        else:
            t2s[ct] = cs
    return True

# Tests
def test_isIsomorphic():
    assert isIsomorphic("egg", "add") == True
    assert isIsomorphic("foo", "bar") == False
    assert isIsomorphic("paper", "title") == True
    assert isIsomorphic("ab", "aa") == False
    assert isIsomorphic("", "") == True
    assert isIsomorphic("a", "a") == True
    assert isIsomorphic("abc", "def") == True
    assert isIsomorphic("abc", "dee") == False
    print("All tests passed!")

test_isIsomorphic()
