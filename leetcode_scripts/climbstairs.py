def climb_stairs(n):
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

def test_climb_stairs():
    assert climb_stairs(1) == 1     # Only one way
    assert climb_stairs(2) == 2     # (1+1) or (2)
    assert climb_stairs(3) == 3     # (1+1+1), (1+2), (2+1)
    assert climb_stairs(4) == 5     # (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)
    assert climb_stairs(5) == 8     # Ways: 8
    assert climb_stairs(0) == 0     # No steps, zero way
    print("All tests passed!")

if __name__ == "__main__":
    test_climb_stairs()
