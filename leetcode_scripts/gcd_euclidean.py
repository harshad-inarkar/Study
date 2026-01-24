def gcd(a, b):
    """
    Computes the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return abs(a)

# Example usage and tests
def test_gcd():
    assert gcd(18, 48) == 6
    assert gcd(48, 18) == 6
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(7, 13) == 1
    assert gcd(-24, 18) == 6
    assert gcd(270, 192) == 6
    assert gcd(100, 10) == 10
    print("All tests passed for gcd.")

if __name__ == "__main__":
    test_gcd()
