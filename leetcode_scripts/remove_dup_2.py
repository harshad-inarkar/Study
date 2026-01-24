def remove_duplicates_2(nums: list[int]) -> int:
    """
    Remove duplicates from sorted array, allowing up to 2 occurrences of each element.
    Elements should be placed at start of array in order.
    
    Parameters:
        nums: List[int] - Sorted array to modify
    Returns:
        int - Length of array after removing excess duplicates
    """
    if len(nums) <= 2:
            return len(nums)

    k = 2  # Start from index 2 since the first two can always stay
    for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

    return k

# Example usage
if __name__ == "__main__":
    nums = [1, 1, 1,1, 2, 2,2, 3,4,4]
    k = remove_duplicates_2(nums)
    print(f"Array after removing excess duplicates: {nums[:k]}")  # Output: [1, 1, 2, 2, 3]
    print(f"New length: {k}")  # Output: 5
