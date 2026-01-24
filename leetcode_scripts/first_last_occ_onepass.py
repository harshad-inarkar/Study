def find_occurrence(nums, target, find_first):
    """
    Helper function to find the first or last occurrence of target in nums.
    If find_first is True, finds first occurrence; else finds last occurrence.
    Returns index if found, else -1.
    """
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            if find_first:
                right = mid - 1
            else:
                left = mid + 1
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
    left, right = 0, len(nums)-1
    first = last = -1

    while left <= right:
        mid = (left+right) >> 1
        if nums[mid] == target:
            first = last = mid
            l,r = mid-1, mid+1
            while l >= left and nums[l] == target :
                first = l
                l-=1
            
            while r <= right and nums[r] == target :
                last = r
                r+=1

            return (first, last)

        elif target < nums[mid]:
            right = mid -1
        else:
            left = mid +1
        

    return (first,last)

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
    # Test 9: Target at end
    assert find_first_and_last([1,2,3,4,5], 5) == (4,4)
    # Test 10: Target in the middle
    assert find_first_and_last([1,2,3,3,3,4,5], 3) == (2,4)
    print("All test cases passed!")

test_find_first_and_last()
