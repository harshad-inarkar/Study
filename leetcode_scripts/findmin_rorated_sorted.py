def find_min_in_rotated_sorted_array(nums):
    """
    Finds the minimum element in a rotated sorted array.
    Assumes no duplicate elements.
    Returns the minimum value.
    """
    if not nums:
        raise ValueError("Input array is empty")
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid +1
        else:
            right = mid
    return nums[left]

# Tests
def test_find_min_in_rotated_sorted_array():
    # Test 1: No rotation
    assert find_min_in_rotated_sorted_array([1,2,3,4,5]) == 1
    # Test 2: Rotated, min in middle
    assert find_min_in_rotated_sorted_array([4,5,6,7,0,1,2]) == 0
    # Test 3: Rotated, min at end
    assert find_min_in_rotated_sorted_array([2,3,4,5,1]) == 1
    # Test 4: Single element
    assert find_min_in_rotated_sorted_array([10]) == 10
    # Test 5: Two elements, rotated
    assert find_min_in_rotated_sorted_array([2,1]) == 1
    # Test 6: Two elements, not rotated
    assert find_min_in_rotated_sorted_array([1,2]) == 1
    # Test 7: Large rotation
    assert find_min_in_rotated_sorted_array([5,6,7,8,9,1,2,3,4]) == 1
    # Test 8: Already sorted
    assert find_min_in_rotated_sorted_array([0,1,2,3,4,5]) == 0
    # Test 9: Empty array raises error
    try:
        find_min_in_rotated_sorted_array([])
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    print("All test cases passed!")

test_find_min_in_rotated_sorted_array()
