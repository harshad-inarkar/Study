def minSubArrayLen(target, nums):
    """
    Returns the minimal length of a contiguous subarray of which the sum ≥ target.
    If there is no such subarray, returns 0.
    """
    n = len(nums)
    left = 0
    total = 0
    min_len = float('inf')
    for right in range(n):
        total += nums[right]
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if min_len == float('inf') else min_len

# Test cases
def test_minSubArrayLen():
    assert minSubArrayLen(7, [2,3,1,2,4,3]) == 2  # [4,3]
    assert minSubArrayLen(4, [1,4,4]) == 1        # [4]
    assert minSubArrayLen(11, [1,2,3,4,5]) == 3   # [3,4,5]
    assert minSubArrayLen(15, [1,2,3,4,5]) == 5   # [1,2,3,4,5]
    assert minSubArrayLen(100, [1,2,3,4,5]) == 0  # no such subarray
    assert minSubArrayLen(3, [1,1]) == 0          # no such subarray
    assert minSubArrayLen(1, [1]) == 1            # [1]
    print("All test cases passed!")

test_minSubArrayLen()
