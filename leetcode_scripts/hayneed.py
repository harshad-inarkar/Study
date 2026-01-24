def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack)-len(needle)+1):
        j=0
        while j < len(needle):
            if haystack[i+j]!= needle[j]:
                break
            j+=1
        if j == len(needle):
            return i

    return -1

# Test cases
def test_strStr():
    # Test case 1: Basic case
    assert strStr("hello", "ll") == 2
    
    # Test case 2: Needle not found
    assert strStr("hello", "world") == -1
    
    # Test case 3: Empty needle
    assert strStr("hello", "") == 0
    
    # Test case 4: Empty haystack
    assert strStr("", "needle") == -1
    
    # Test case 5: Needle at start
    assert strStr("needle", "need") == 0
    
    # Test case 6: Needle at end
    assert strStr("haystack", "stack") == 3
    
    print("All test cases passed!")

# Run the tests
test_strStr()
