def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Returns indices of the two numbers such that they add up to target.
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []


# Test case
def test_twoSum():
    assert twoSum([2,7,11,15], 9) == [0,1]
    assert twoSum([3,2,4], 6) == [1,2]
    assert twoSum([3,3], 6) == [0,1]
    assert twoSum([1,2,3], 7) == []
    print("All test cases passed!")

test_twoSum()
