def longest_palindromic_substring_center(s):
    """
    Returns the longest palindromic substring in s using center expansion.
    """
    if not s:
        return ""
    start, end = 0, 0

    def expand_around_center(left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Exited: s[left] != s[right], so actual palindrome is s[left+1:right]
        return left+1, right-1

    for i in range(len(s)):
        # Odd length
        l1, r1 = expand_around_center(i, i)
        # Even length
        l2, r2 = expand_around_center(i, i+1)
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2
    return s[start:end+1]

def test_longest_palindromic_substring_center():
    assert longest_palindromic_substring_center("babad") in ("bab", "aba")
    assert longest_palindromic_substring_center("cbbd") == "bb"
    assert longest_palindromic_substring_center("a") == "a"
    assert longest_palindromic_substring_center("") == ""
    assert longest_palindromic_substring_center("racecar") == "racecar"
    assert longest_palindromic_substring_center("forgeeksskeegfor") == "geeksskeeg"
    assert longest_palindromic_substring_center("abacab") == "bacab"
    assert longest_palindromic_substring_center("abccba") == "abccba"
    assert longest_palindromic_substring_center("abcd") in ("a", "b", "c", "d")
    print("All tests passed!")

if __name__ == "__main__":
    test_longest_palindromic_substring_center()
