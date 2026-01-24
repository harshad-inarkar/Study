def permute(nums):
    """
    Returns all possible permutations of the list nums.
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []

    n = len(nums)
  

    def backtrack(pathlen):
        if pathlen == n:
            res.append(nums[:])
            return
        
        for i in range(pathlen,n):
            nums[pathlen],nums[i] = nums[i], nums[pathlen]
            backtrack(pathlen+1)
            nums[pathlen],nums[i] = nums[i], nums[pathlen]

    backtrack(0)
    return res

# Tests
def test_permute():
    assert sorted(permute([1,2,3])) == sorted([
        [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]
    ]), "Test 1 failed"
    assert permute([0]) == [[0]], "Test 2 failed"
    assert permute([]) == [[]], "Test 3 failed"
    assert sorted(permute([1,2])) == sorted([[1,2],[2,1]]), "Test 4 failed"
    print("All tests passed.")

if __name__ == "__main__":
    test_permute()
