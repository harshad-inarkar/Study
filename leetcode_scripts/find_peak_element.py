def find_peak_element(nums):
    """
    Finds a peak element in the array and returns its index.
    A peak element is an element that is strictly greater than its neighbors.
    If the array contains multiple peaks, return the index to any of the peaks.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

# Tests
def test_find_peak_element():
    # Test 1: Single peak in the middle
    nums1 = [1, 2, 3, 1]
    idx1 = find_peak_element(nums1)
    assert nums1[idx1] == 3

    # Test 2: Peak at the end
    nums2 = [1, 2, 1, 3, 5, 6, 4]
    idx2 = find_peak_element(nums2)
    # The peak can be 6 (index 5) or 2 (index 1)
    assert nums2[idx2] in (2, 6)

    # Test 3: Single element
    nums3 = [1]
    idx3 = find_peak_element(nums3)
    assert idx3 == 0

    # Test 4: Two elements, increasing
    nums4 = [1, 2]
    idx4 = find_peak_element(nums4)
    assert idx4 == 1

    # Test 5: Two elements, decreasing
    nums5 = [2, 1]
    idx5 = find_peak_element(nums5)
    assert idx5 == 0

    # Test 6: All elements equal (any index is a peak)
    nums6 = [3, 3, 3, 3]
    idx6 = find_peak_element(nums6)
    assert 0 <= idx6 < len(nums6)

    # Test 7: Peak at the start
    nums7 = [5, 4, 3, 2, 1]
    idx7 = find_peak_element(nums7)
    assert idx7 == 0

    print("All test cases passed!")

test_find_peak_element()
