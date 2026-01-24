def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    """
    Returns True if there are two distinct indices i and j in the array such that
    nums[i] == nums[j] and abs(i - j) <= k, using a sliding window.
    """
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
    return False

# Tests
def test_containsNearbyDuplicate():
    assert containsNearbyDuplicate([1,2,3,1], 3) == True
    assert containsNearbyDuplicate([1,0,1,1], 1) == True
    assert containsNearbyDuplicate([1,2,3,1,2,3], 2) == False
    assert containsNearbyDuplicate([], 1) == False
    assert containsNearbyDuplicate([99,99], 2) == True
    assert containsNearbyDuplicate([1,2,3,4,5], 0) == False
    assert containsNearbyDuplicate([1,2,3,1,2,3], 3) == True
    print("All tests passed!")

test_containsNearbyDuplicate()

