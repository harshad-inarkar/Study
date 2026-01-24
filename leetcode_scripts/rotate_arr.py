def rotate_array(nums: list[int], k: int) -> None:
    """
    Rotate the array to the right by k steps in-place.
    
    Parameters:
        nums: List[int] - Array to rotate
        k: int - Number of steps to rotate
    Returns:
        None - Array is modified in-place
    """
    k = k % len(nums)  # Handle cases where k > n
    
    # Reverse entire array
    nums[:] = nums[-k:] + nums[:-k]

#   nums[:] = nums[k:] + nums[:k]

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate_array(nums, k)
    print(f"Array after rotating by {k} steps: {nums}")  # Output: [5, 6, 7, 1, 2, 3, 4]


