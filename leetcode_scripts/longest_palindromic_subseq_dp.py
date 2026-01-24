def longest_palindromic_subsequence(s):
    """
    Returns the length of the longest palindromic subsequence in s.
    """
    n = len(s)
    if n == 0:
        return 0
    dp = [[0]*n for _ in range(n)]
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4  # "bbbb"
    assert longest_palindromic_subsequence("cbbd") == 2   # "bb"
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("") == 0
    assert longest_palindromic_subsequence("agbdba") == 5  # "abdba"
    assert longest_palindromic_subsequence("abcdefg") == 1
    assert longest_palindromic_subsequence("aaaaaa") == 6  # entire string
    assert longest_palindromic_subsequence("racecar") == 7 # entire string
    print("All tests passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()
