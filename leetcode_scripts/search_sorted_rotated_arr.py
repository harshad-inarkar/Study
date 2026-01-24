def search_in_rotated_sorted_array(nums, target):
    """
    Searches for a target value in a rotated sorted array.
    Returns the index if found, else -1.
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Tests
def test_search_in_rotated_sorted_array():
    # Test 1: Target present, no rotation
    assert search_in_rotated_sorted_array([1,2,3,4,5,6], 4) == 3
    # Test 2: Target present, rotated
    assert search_in_rotated_sorted_array([4,5,6,7,0,1,2], 0) == 4
    # Test 3: Target not present
    assert search_in_rotated_sorted_array([4,5,6,7,0,1,2], 3) == -1
    # Test 4: Single element, target present
    assert search_in_rotated_sorted_array([1], 1) == 0
    # Test 5: Single element, target not present
    assert search_in_rotated_sorted_array([1], 0) == -1
    # Test 6: Empty array
    assert search_in_rotated_sorted_array([], 5) == -1
    # Test 7: Target at start
    assert search_in_rotated_sorted_array([6,7,8,1,2,3,4,5], 6) == 0
    # Test 8: Target at end
    assert search_in_rotated_sorted_array([6,7,8,1,2,3,4,5], 5) == 7
    # Test 9: All elements same except one
    assert search_in_rotated_sorted_array([2,2,2,3,2,2], 3) == 3
    # Test 10: Two elements, rotated
    assert search_in_rotated_sorted_array([5,1], 1) == 1
    print("All test cases passed!")

test_search_in_rotated_sorted_array()
