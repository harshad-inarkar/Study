def minWindow(s: str, t: str) -> str:
    """
    Returns the minimum window substring of s such that every character in t (including duplicates) is included in the window.
    If no such window exists, returns an empty string.
    """
    if not s or not t:
        return ''
    counter_t = {}
    for ch in t:
        counter_t[ch] = counter_t.get(ch,0)+1
    
    req = len(counter_t)
    formed = 0
    l = 0
    win_len = float('inf')
    win_l,win_r = 0,0
    counter_win = {}
    for r, c in enumerate(s):
        counter_win[c] = counter_win.get(c,0)+1
        if c in counter_t and counter_t[c] == counter_win[c]:
            formed+=1
        
        while l<=r and formed == req:
            
            if r - l +1 < win_len:
                win_len = r - l+1
                win_l = l
                win_r = r

            counter_win[s[l]] -=1
            if s[l] in  counter_t and counter_win[s[l]] < counter_t[s[l]]:
                formed-=1
            
            l+=1
    
    return '' if win_len == float('inf') else s[win_l:win_r+1]



# Test cases
def test_minWindow():
    assert minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert minWindow("a", "a") == "a"
    assert minWindow("a", "aa") == ""
    assert minWindow("ab", "A") == ""
    assert minWindow("bba", "ab") == "ba"
    assert minWindow("aa", "aa") == "aa"
    assert minWindow("abc", "cba") == "abc"
    assert minWindow("abdecfab", "fab") == "fab"
    print("All test cases passed!")

test_minWindow()
