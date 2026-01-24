def is_palindrome_number(x):
    """
    Returns True if x is a palindrome number, False otherwise.
    Negative numbers are not palindromes.
    """
    if x < 0 or (x%10 == 0 and x !=0):
        return False

    reversed_half = 0   
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return  (x == reversed_half) or (x == reversed_half//10)

# Example usage and tests
def test_is_palindrome_number():
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(-121) == False
    assert is_palindrome_number(10) == False
    assert is_palindrome_number(0) == True
    assert is_palindrome_number(12321) == True
    print("All tests passed for is_palindrome_number.")

if __name__ == "__main__":
    test_is_palindrome_number()
