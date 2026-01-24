def myPow(x, n):
    """
    Computes x raised to the power n (x^n).
    Handles negative exponents.
    """
    orig_n = n
    if n < 0:
        n = -n

    result = 1.0
    while n:
        if n &1:
            result *= x
        x *= x
        n=n>>1

    return 1/result if orig_n < 0 else result

# Example usage and tests
def test_myPow():
    assert abs(myPow(2.0, 10) - 1024.0) < 1e-9
    assert abs(myPow(2.1, 3) - 9.261) < 1e-3
    assert abs(myPow(2.0, -2) - 0.25) < 1e-9
    assert abs(myPow(0.0, 0) - 1.0) < 1e-9
    assert abs(myPow(1.0, 1000) - 1.0) < 1e-9
    print("All tests passed for myPow.")

if __name__ == "__main__":
    test_myPow()
