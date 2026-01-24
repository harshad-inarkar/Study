def length_of_lis(nums):
    """
    Returns the length of the longest increasing subsequence in the list nums.
    """
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def test_length_of_lis():
    assert length_of_lis([10,9,2,5,3,7,101,18]) == 4  # [2,3,7,101]
    assert length_of_lis([0,1,0,3,2,3]) == 4          # [0,1,2,3]
    assert length_of_lis([7,7,7,7,7,7,7]) == 1        # [7]
    assert length_of_lis([1,3,6,7,9,4,10,5,6]) == 6   # [1,3,6,7,9,10] or similar
    assert length_of_lis([]) == 0                     # Empty list
    assert length_of_lis([1]) == 1                    # Single element
    assert length_of_lis([3,2,1]) == 1                # Decreasing
    print("All tests passed!")

if __name__ == "__main__":
    test_length_of_lis()
