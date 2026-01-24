def search_insert_position(nums, target):
    """
    Given a sorted array and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Tests
def test_search_insert_position():
    # Test 1: Target present
    assert search_insert_position([1,3,5,6], 5) == 2
    # Test 2: Target not present, insert at end
    assert search_insert_position([1,3,5,6], 7) == 4
    # Test 3: Target not present, insert at start
    assert search_insert_position([1,3,5,6], 0) == 0
    # Test 4: Target not present, insert in middle
    assert search_insert_position([1,3,5,6], 2) == 1
    # Test 5: Empty array
    assert search_insert_position([], 3) == 0
    # Test 6: Single element, target less
    assert search_insert_position([5], 2) == 0
    # Test 7: Single element, target more
    assert search_insert_position([5], 8) == 1
    # Test 8: Single element, target equal
    assert search_insert_position([5], 5) == 0
    # Test 9: All elements less than target
    assert search_insert_position([1,2,3], 10) == 3
    # Test 10: All elements greater than target
    assert search_insert_position([4,5,6], 1) == 0
    print("All test cases passed!")

test_search_insert_position()
