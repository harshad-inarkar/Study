def findMedianSortedArrays(nums1, nums2):
    """
    Finds the median of two sorted arrays.
    Time complexity: O(log(min(m, n)))
    """
    m,n = len(nums1), len(nums2)

    if m > n :
        nums1,nums2, m,n = nums2, nums1, n,m

    
    l, h, total = 0,m, m+n
    half_len = (total+1) >>1

    while l <=h:
        part1 = (l+h) >> 1
        part2 = half_len - part1

        lmax1 = nums1[part1-1] if part1 != 0  else float('-inf')
        lmax2 = nums2[part2-1] if part2 != 0 else float('-inf')
        rmin1 = nums1[part1] if part1 != m else float('inf')
        rmin2 = nums2[part2] if part2 != n else float('inf')

        if lmax1 <= rmin2 and lmax2 <= rmin1:
            if total&1 == 0:
                return ((lmax1 if lmax1 > lmax2 else lmax2) + (rmin1 if rmin1 < rmin2 else rmin2))/2
            else:
                return lmax1 if lmax1 > lmax2 else lmax2
        elif lmax1 >  rmin2:
            h = part1-1
        else:
            l = part1+1


# Test cases
def test_findMedianSortedArrays():
    # Odd total length
    assert findMedianSortedArrays([1,3], [2]) == 2
    # Even total length
    assert findMedianSortedArrays([1,2], [3,4]) == 2.5
    # One array empty
    assert findMedianSortedArrays([], [1]) == 1
    assert findMedianSortedArrays([2], []) == 2
    # Both arrays have one element
    assert findMedianSortedArrays([1], [2]) == 1.5
    # Arrays with duplicates
    assert findMedianSortedArrays([1,2,2], [2,2,3]) == 2
    # Large arrays
    assert findMedianSortedArrays(list(range(1000)), list(range(1000,2000))) == 999.5
    # Both arrays empty should raise error

    print("All test cases passed!")

test_findMedianSortedArrays()
