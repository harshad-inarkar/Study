def maxNumberOfKSumPairs(nums, k):
    """
    Returns the maximum number of unique k-sum pairs (i, j) in the array nums such that
    nums[i] + nums[j] == k and each element can only be used once.
    """
    from collections import Counter
    count = Counter(nums)
    pairs = 0

    for x in list(count.keys()):
        complement = k - x
        if complement in count:
            if x == complement:
                pairs += count[x] // 2
            elif x < complement:  # ensure each pair counted once
                pairs += min(count[x], count[complement])
    return pairs

# Example tests
def test_maxNumberOfKSumPairs():
    assert maxNumberOfKSumPairs([1,2,3,4], 5) == 2  # (1,4), (2,3)
    assert maxNumberOfKSumPairs([3,1,3,4,3], 6) == 1  # (3,3)
    assert maxNumberOfKSumPairs([1,1,1,2,2,2], 3) == 3  # (1,2) three times
    assert maxNumberOfKSumPairs([1,5,1,5], 6) == 2  # (1,5), (1,5)
    assert maxNumberOfKSumPairs([], 4) == 0
    assert maxNumberOfKSumPairs([2,2,2,2], 4) == 2  # (2,2) twice
    print("All tests passed for maxNumberOfKSumPairs.")

if __name__ == "__main__":
    test_maxNumberOfKSumPairs()
