# Robber algorithm implementation (maximum sum of non-adjacent numbers)
def rob(nums):
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]
    dp0, dp1 = 0, nums[0]
    for i in range(1, n):
        temp = dp1
        dp1 = max(dp1, dp0 + nums[i])
        dp0 = temp
    return dp1

# Test cases
def test_rob():
    assert rob([1,2,3,1]) == 4   # rob 1st and 3rd house
    assert rob([2,7,9,3,1]) == 12  # rob 2nd and 4th house
    assert rob([2,1,1,2]) == 4     # rob 1st and 4th house
    assert rob([]) == 0            # no house
    assert rob([5]) == 5           # single house
    assert rob([1,3,1]) == 3
    assert rob([2,1,4,9]) == 11    # rob 1st and 4th house
    print("All tests passed!")

if __name__ == "__main__":
    test_rob()
