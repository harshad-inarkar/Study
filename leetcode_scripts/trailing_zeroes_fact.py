def trailing_zeroes_in_factorial(n):
    """
    Returns the number of trailing zeroes in n!
    """
    count= 0
    while n > 0:
        n = n//5
        count += n

    return count

# Example usage and tests
def test_trailing_zeroes_in_factorial():
    assert trailing_zeroes_in_factorial(0) == 0
    assert trailing_zeroes_in_factorial(5) == 1
    assert trailing_zeroes_in_factorial(10) == 2
    assert trailing_zeroes_in_factorial(25) == 6
    assert trailing_zeroes_in_factorial(100) == 24
    
    print("All tests passed for trailing_zeroes_in_factorial.")

if __name__ == "__main__":
    test_trailing_zeroes_in_factorial()
