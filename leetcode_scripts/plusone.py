def plus_one(digits):
    """
    Given a non-empty list of decimal digits representing a non-negative integer, increment one to the integer.
    The digits are stored such that the most significant digit is at the head of the list.
    """
    n = len(digits)
    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    # If all digits were 9
    return [1] + digits

# Example usage and tests
def test_plus_one():
    assert plus_one([1,2,3]) == [1,2,4]
    assert plus_one([4,3,2,1]) == [4,3,2,2]
    assert plus_one([9]) == [1,0]
    assert plus_one([9,9,9]) == [1,0,0,0]

