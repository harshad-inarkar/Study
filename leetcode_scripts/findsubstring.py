def findSubstring(s, words):
    """
    Returns all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
    """
    if not s or not words or not words[0]:
        return []
    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    res = []
    for i in range(word_len):
        left = i
        right = i
        curr_count = {}
        count = 0
        while right + word_len <= len(s):
            word = s[right:right+word_len]
            right += word_len
            if word in word_count:
                curr_count[word] = curr_count.get(word, 0) + 1
                count += 1
                while curr_count[word] > word_count[word]:
                    left_word = s[left:left+word_len]
                    curr_count[left_word] -= 1
                    left += word_len
                    count -= 1
                if count == num_words:
                    res.append(left)
            else:
                curr_count.clear()
                count = 0
                left = right
    return res

# Test cases
def test_findSubstring():
    assert findSubstring("barfoothefoobarman", ["foo","bar"]) == [0,9]
    assert findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]) == []
    assert findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]) == [6,9,12]
    assert findSubstring("aaaaaa", ["aa","aa","aa"]) == [0]
    assert findSubstring("", ["a"]) == []
    assert findSubstring("a", []) == []
    assert findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]) == [13]
    print("All test cases passed!")

test_findSubstring()
