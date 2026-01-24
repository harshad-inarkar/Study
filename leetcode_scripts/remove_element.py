def remove_element(nums: list[int], val: int) -> int:
    """
    Remove all occurrences of val in nums in-place and return new length.
    The order of elements can be changed.
    
    Parameters:
        nums: List[int] - Array to modify
        val: int - Value to remove
    Returns:
        int - New length after removing val
    """
    k = 0  # Position to place next kept element
    
    # Iterate through array
    for i in range(len(nums)):
        # If current element is not val, keep it
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
            
    return k

# Example usage
if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    k = remove_element(nums, val)
    print(f"Array after removing {val}: {nums[:k]}")  # Output: [2, 2]
    print(f"New length: {k}")  # Output: 2
