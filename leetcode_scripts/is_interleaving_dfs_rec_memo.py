


from functools import lru_cache


def is_interleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    @lru_cache(None)
    def dfs(i, j):
        k = i + j
        if k == len(s3):
            return True

        # Option 1: Take from s1 if it matches
        if i < len(s1) and s1[i] == s3[k]:
            if dfs(i + 1, j):
                return True

        # Option 2: Take from s2 if it matches
        if j < len(s2) and s2[j] == s3[k]:
            if dfs(i, j + 1):
                return True

        return False

    return dfs(0, 0)


def test_is_interleave():
    assert is_interleave("aabcc", "dbbca", "aadbbcbcac") == True
    assert is_interleave("aabcc", "dbbca", "aadbbbaccc") == False
    assert is_interleave("", "", "") == True
    assert is_interleave("abc", "", "abc") == True
    assert is_interleave("", "abc", "abc") == True
    assert is_interleave("abc", "def", "adbcef") == True
    assert is_interleave("abc", "def", "abdecf") == True
    assert is_interleave("abc", "def", "abdefc") == True
    assert is_interleave("a", "b", "ab") == True
    assert is_interleave("a", "b", "ba") == True
    assert is_interleave("aa", "ab", "aaba") == True
    print("All tests passed for is_interleave.")

if __name__ == "__main__":
    test_is_interleave()
