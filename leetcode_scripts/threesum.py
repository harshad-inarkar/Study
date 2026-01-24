def threeSum(nums):
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
    i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.
    """
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # skip duplicates for i
        l, r = i+1, n-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1  # skip duplicates for l
                while l < r and nums[r] == nums[r+1]:
                    r -= 1  # skip duplicates for r
    return res

# Test cases
def test_threeSum():
    assert sorted(threeSum([-1,0,1,2,-1,-4])) == sorted([[-1,-1,2],[-1,0,1]])
    assert threeSum([]) == []
    assert threeSum([0]) == []
    assert sorted(threeSum([0,0,0])) == [[0,0,0]]
    assert sorted(threeSum([1,2,-2,-1])) == []
    print("All test cases passed!")

test_threeSum()
