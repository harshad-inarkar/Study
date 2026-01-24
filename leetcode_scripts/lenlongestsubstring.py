def lengthOfLongestSubstring(s):
    """
    Returns the length of the longest substring without repeating characters.
    """
    char_index = {}
    left = 0
    max_len = 0
    for right, c in enumerate(s):
        if c in char_index and char_index[c] >= left:
            left = char_index[c] + 1
        char_index[c] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# Test cases
def test_lengthOfLongestSubstring():
    assert lengthOfLongestSubstring("abcabcbb") == 3  # "abc"
    assert lengthOfLongestSubstring("bbbbb") == 1     # "b"
    assert lengthOfLongestSubstring("pwwkew") == 3    # "wke"
    assert lengthOfLongestSubstring("") == 0
    assert lengthOfLongestSubstring("dvdf") == 3      # "vdf"
    assert lengthOfLongestSubstring("aab") == 2       # "ab"
    print("All test cases passed!")

test_lengthOfLongestSubstring()
