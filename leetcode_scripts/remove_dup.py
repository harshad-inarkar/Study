def remove_duplicates(nums: list[int]) -> int:
    """
    Remove duplicates in-place from sorted array and return new length.
    Elements should be placed at start of array in order.
    
    Parameters:
        nums: List[int] - Sorted array to modify
    Returns:
        int - Length of array after removing duplicates
    """
    if not nums:
        return 0
        
    k = 0  # Position to place next unique element
    
    # Compare adjacent elements
    for i in range(1, len(nums)):
        # If current element differs from previous, keep it
        if nums[i] != nums[k]:
            k+=1
            nums[k] = nums[i]
            
    return k+1

# Example usage
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 4, 4]
    k = remove_duplicates(nums)
    print(f"Array after removing duplicates: {nums[:k]}")  # Output: [1, 2, 3, 4]
    print(f"New length: {k}")  # Output: 4
