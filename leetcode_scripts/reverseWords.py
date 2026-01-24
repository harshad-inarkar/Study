def reverseWords(s: str) -> str:   
    def reverseWords(self, s: str) -> str:
        return ' '.join([w for w in s.split()[::-1] if w])
    
    
# Test cases
def test_reverseWords():
    # Test case 1: Basic sentence
    assert reverseWords("the sky is blue") == "blue is sky the"
    
    # Test case 2: Multiple spaces between words
    assert reverseWords("  hello world  ") == "world hello"
    
    # Test case 3: Single word
    assert reverseWords("hello") == "hello"
    
    # Test case 4: Empty string
    assert reverseWords("") == ""
    
    # Test case 5: String with only spaces
    assert reverseWords("   ") == ""
    
    print("All test cases passed!")

# Run the tests
test_reverseWords()
