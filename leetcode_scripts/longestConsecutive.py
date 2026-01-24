def longestConsecutive(nums):
    """
    Returns the length of the longest consecutive elements sequence.
    """
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting if num is the start of a sequence
        if num - 1 not in num_set:
            current = num
            streak = 1
            while current + 1 in num_set:
                current += 1
                streak += 1
            longest = max(longest, streak)
    return longest

# Tests
def test_longestConsecutive():
    assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4  # [1,2,3,4]
    assert longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9   # [0,1,2,3,4,5,6,7,8]
    assert longestConsecutive([]) == 0
    assert longestConsecutive([1,2,0,1]) == 3
    assert longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]) == 7  # [-1,0,1,3,4,5,6,7,8,9]
    assert longestConsecutive([1]) == 1
    print("All tests passed!")

test_longestConsecutive()
