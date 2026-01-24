def max_sub_array(nums):
    """
    Finds the contiguous subarray with the largest sum.
    Uses Kadane's algorithm.
    """
    if not nums:
        return 0
        
    curr_sum = max_sum = nums[0]

    for i in range(1,len(nums)):
        n = nums[i]
        curr_sum+=n
        if curr_sum < n:
            curr_sum = n
        
        if max_sum < curr_sum:
            max_sum = curr_sum

    
    return max_sum

# Tests
def test_max_sub_array():
    # Test 1: Empty array
    assert max_sub_array([]) == 0

    # Test 2: All positive numbers
    assert max_sub_array([10, 2, -1, 4,-3]) == 15

    # Test 3: All negative numbers
    assert max_sub_array([-1, -2, -3, -4]) == -1

    # Test 4: Mixed positive and negative
    assert max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) == 6  # [4,-1,2,1]

    # Test 5: Single element
    assert max_sub_array([5]) == 5
    assert max_sub_array([-5]) == -5

    # Test 6: Large negative followed by positives
    assert max_sub_array([-10, 2, 3, 1]) == 6

    # Test 7: Zeros
    assert max_sub_array([0, 0, 0, 0]) == 0

    # Test 8: Subarray at the end
    assert max_sub_array([-2, -3, 4, 5, -1, 2]) == 10

test_max_sub_array()
