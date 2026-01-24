def mySqrt(x):
    """
    Computes and returns the integer square root of a non-negative integer x.
    The integer square root is the greatest integer less than or equal to the true square root.
    """
    if x < 2:
        return x

    left, right = 1, x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right

# Example usage and tests
def test_mySqrt():
    assert mySqrt(0) == 0
    assert mySqrt(1) == 1
    assert mySqrt(4) == 2
    assert mySqrt(8) == 2
    assert mySqrt(16) == 4
    assert mySqrt(27) == 5
    assert mySqrt(2147395599) == 46339
    print("All tests passed for mySqrt.")

if __name__ == "__main__":
    test_mySqrt()
