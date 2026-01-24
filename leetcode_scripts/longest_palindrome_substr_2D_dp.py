def longest_palindromic_substring(s):
    """
    Returns the longest palindromic substring of s using dynamic programming.
    """
    n = len(s)
    dp = [[False] *n for _ in range(n)]
    start, max_len =0, 1

    for i in range(n):
        dp[i][i] = True

    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1

            if s[i] == s[j]:
                if l <=2 or dp[i+1][j-1] == True:
                    dp[i][j] = True
                    if l > max_len:
                        start, max_len= i, l
    

    return s[start:start+max_len]


def test_longest_palindromic_substring():
    assert longest_palindromic_substring("babad") in ("bab", "aba")
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"
    assert longest_palindromic_substring("abacab") == "bacab"
    assert longest_palindromic_substring("abccba") == "abccba"
    assert longest_palindromic_substring("abcd") in ("a", "b", "c", "d")
    print("All tests passed!")

if __name__ == "__main__":
    test_longest_palindromic_substring()


