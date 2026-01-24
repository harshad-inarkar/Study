def find_occ(nums,target,isfirst):
    """
    Finds the first occurrence of target in a sorted array nums.
    Returns the index if found, else -1.
    """
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            if isfirst:
                right = mid - 1
            else:
                left = mid+1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result



def find_first_and_last(nums, target):
    """
    Returns a tuple (first_index, last_index) for the first and last occurrence of target.
    If not found, returns (-1, -1).
    """
    return (find_occ(nums, target,True), find_occ(nums, target,False))

# Tests
def test_find_first_and_last():
    # Test 1: Target present multiple times
    assert find_first_and_last([5,7,7,8,8,10], 8) == (3,4)
    # Test 2: Target present once
    assert find_first_and_last([5,7,7,8,8,10], 10) == (5,5)
    # Test 3: Target not present
    assert find_first_and_last([5,7,7,8,8,10], 6) == (-1,-1)
    # Test 4: All elements are target
    assert find_first_and_last([2,2,2,2,2], 2) == (0,4)
    # Test 5: Empty array
    assert find_first_and_last([], 1) == (-1,-1)
    # Test 6: Single element, is target
    assert find_first_and_last([3], 3) == (0,0)
    # Test 7: Single element, not target
    assert find_first_and_last([3], 2) == (-1,-1)
    # Test 8: Target at start
    assert find_first_and_last([1,2,3,4,5], 1) == (0,0)

