def word_break(s, word_dict):
    """
    Returns True if string s can be segmented into a space-separated sequence of one or more dictionary words.
    """
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True  # empty string
    
    for i in range(1, len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]

def test_word_break():
    assert word_break("leetcode", ["leet", "code"]) == True  # "leet code"
    assert word_break("applepenapple", ["apple", "pen"]) == True  # "apple pen apple"
    assert word_break("catsandog", ["cats","dog","sand","and","cat"]) == False
    assert word_break("", ["a"]) == True  # empty string is segmentable
    assert word_break("a", ["b"]) == False
    assert word_break("a", ["a"]) == True
    assert word_break("cars", ["car","ca","rs"]) == True  # "ca rs"
    assert word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                      ["a","aa","aaa","aaaa","aaaaa","aaaaaa"]) == False
    print("All tests passed!")

if __name__ == "__main__":
    test_word_break()
