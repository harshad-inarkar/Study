def is_interleave(s1, s2, s3):
    """
    Returns True if s3 is formed by the interleaving of s1 and s2.
    Uses DP with O(m*n) time and space.
    """
    m, n = len(s1), len(s2)
    if len(s3) != m + n:
        return False

    dp = [[False] * (n+1) for _ in range(m+1)]
    dp[0][0] = True

    for j in range(1,n+1):
        dp[0][j] = dp[0][j-1] and s3[j-1] == s2[j-1]
    

    for i in range(1,m+1):
        dp[i][0] = dp[i-1][0] and s3[i-1] == s1[i-1]


    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or  \
                (dp[i][j-1] and s2[j-1] == s3[i+j-1])


    return dp[m][n]


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
