def sum_of_digits(n):
    """
    Given a two-digit integer n, return the sum of its digits.
    """
    return abs(n) // 10 + abs(n) % 10

# Example usage and simple tests
if __name__ == "__main__":
    assert sum_of_digits(42) == 6
    assert sum_of_digits(99) == 18
    assert sum_of_digits(-34) == 7
    print("All tests passed!")
