def max_subarray_sum_circular(nums):
    """
    Finds the maximum sum of a non-empty subarray in a circular array.
    """
    if not nums:
        return 0


    curr_max_sum = max_sum = nums[0]
    total= curr_min_sum = min_sum = nums[0]
    
    for i in range(1,len(nums)):
        n = nums[i]
        total+=n
        curr_max_sum+=n
        if curr_max_sum < n:
            curr_max_sum = n
        
        if max_sum < curr_max_sum:
            max_sum = curr_max_sum


        curr_min_sum+=n
        if curr_min_sum > n:
            curr_min_sum = n
        
        if min_sum > curr_min_sum:
            min_sum = curr_min_sum
        
    if max_sum < 0:
        return max_sum
    
    return max(max_sum, total - min_sum)



# Tests
def test_max_subarray_sum_circular():
    # Test 1: All positive numbers
    assert max_subarray_sum_circular([1,2,3,4]) == 10

    # Test 2: All negative numbers
    assert max_subarray_sum_circular([-1,-2,-3,-4]) == -1

    # Test 3: Mixed, max subarray not wrapping
    assert max_subarray_sum_circular([5,-3,5]) == 10

    # Test 4: Mixed, max subarray wraps
    assert max_subarray_sum_circular([3,-1,2,-1]) == 4

    # Test 5: Mixed, max subarray is the whole array
    assert max_subarray_sum_circular([1,-2,3,-2]) == 3

    # Test 6: Single element
    assert max_subarray_sum_circular([7]) == 7
    assert max_subarray_sum_circular([-7]) == -7

    # Test 7: Zeros
    assert max_subarray_sum_circular([0,0,0]) == 0

    # Test 8: Large negative followed by positives
    assert max_subarray_sum_circular([-10, 2, 3, 1]) == 6

    # Test 9: Wrap-around is optimal
    assert max_subarray_sum_circular([8,-1,3,4]) == 15

    # Test 10: Empty array
    assert max_subarray_sum_circular([]) == 0

test_max_subarray_sum_circular()
