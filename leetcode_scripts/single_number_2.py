def single_number_2(nums):
    """
    Given a non-empty array of integers nums, every element appears three times except for one. Find that single one.
    """
    ones, twos = 0, 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones

# Tests
def test_single_number_2():
    assert single_number_2([2, 2, 3, 2]) == 3
    assert single_number_2([0, 1, 0, 1, 0, 1, 99]) == 99
    assert single_number_2([5, 5, 5, 7]) == 7
    assert single_number_2([-2, -2, -2, -9]) == -9
    assert single_number_2([42]) == 42
    print("All tests passed for single_number_2.")

if __name__ == "__main__":
    test_single_number_2()
