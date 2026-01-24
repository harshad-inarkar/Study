def increasing_triplet(nums):
    """
    Returns True if there exists an increasing subsequence of length 3 in nums.
    Uses O(1) space and O(n) time.
    """
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False

def test_increasing_triplet():
    assert increasing_triplet([1,2,3,4,5]) == True      # increasing
    assert increasing_triplet([5,4,3,2,1]) == False     # decreasing
    assert increasing_triplet([2,1,5,0,4,6]) == True    # 1,4,6
    assert increasing_triplet([20,100,10,12,5,13]) == True # 10,12,13
    assert increasing_triplet([1,1,-2,6]) == False
    assert increasing_triplet([2,4,-2,-3]) == False
    assert increasing_triplet([1,2]) == False
    assert increasing_triplet([]) == False
    print("All tests passed for increasing_triplet.")

if __name__ == "__main__":
    test_increasing_triplet()
