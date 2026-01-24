def longestCommonPrefix(strs):
    if not strs:
        return ''

    for i in range(len(strs[0])):
        for st in strs:
            if i == len(st) or st[i] != strs[0][i]:
                return strs[0][:i]

    return strs[0]


# Test cases for longestCommonPrefix function
def test_longestCommonPrefix():
    # Test case 1: Empty list
    assert longestCommonPrefix([]) == ""
    
    # Test case 2: Single string
    assert longestCommonPrefix(["flower"]) == "flower"
    
    # Test case 3: Common prefix exists
    assert longestCommonPrefix(["flower", "flow", "abcde"]) == ""
    
    # Test case 4: No common prefix
    assert longestCommonPrefix(["dog", "racecar", "car"]) == ""
    
    # Test case 5: All strings are same
    assert longestCommonPrefix(["hello", "hello", "hello"]) == "hello"
    
    # Test case 6: Empty strings
    assert longestCommonPrefix(["", "", ""]) == ""
    
    print("All test cases passed!")

# Run the tests
test_longestCommonPrefix()

