def climbStairs(n):
    """
    Returns the number of distinct ways to climb to the top of a staircase with n steps,
    where you can climb either 1 or 2 steps at a time.
    """
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b

# Example usage and tests
def test_climbStairs():
    assert climbStairs(1) == 1
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3
    assert climbStairs(4) == 5
    assert climbStairs(5) == 8
    assert climbStairs(10) == 89
    print("All tests passed for climbStairs.")

if __name__ == "__main__":
    test_climbStairs()
