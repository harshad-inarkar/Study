def single_number(nums):
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    """
    result = 0
    for num in nums:
        result ^= num
    return result

# Tests
def test_single_number():
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1
    assert single_number([0, 0, 7]) == 7
    assert single_number([-1, -1, -2]) == -2
    print("All tests passed.")

if __name__ == "__main__":
    test_single_number()
