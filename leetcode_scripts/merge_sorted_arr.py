def merge_sorted_arrays(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merge nums2 into nums1 in-place as a sorted array.
    nums1 has length m + n with last n elements being 0 to fit nums2.
    
    Parameters:
        nums1: List[int] - First array with extra space at end
        m: int - Number of actual elements in nums1
        nums2: List[int] - Second array to merge
        n: int - Length of nums2
    """
    # Start from the end of both arrays
    last = m + n - 1  # Last position in nums1
    i = m - 1        # Last element in nums1
    j = n - 1        # Last element in nums2
    
    # While there are elements to compare
    while j >= 0:
        # If i >= 0 and nums1[i] is larger, place it at the end
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[last] = nums1[i]
            i -= 1
        # Otherwise place element from nums2
        else:
            nums1[last] = nums2[j]
            j -= 1
        last -= 1

# Example usage
if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge_sorted_arrays(nums1, 3, nums2, 3)
    print(f"Merged array: {nums1}")  # Output: [1, 2, 2, 3, 5, 6]
