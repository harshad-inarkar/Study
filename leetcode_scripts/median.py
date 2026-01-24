def find_median(nums: list[int]) -> float:
    """
    Calculate the median of a list of numbers.
    
    Parameters:
        nums: List[int] - Input array of integers
    Returns:
        float - The median of the list
    """
    if not nums:
        raise ValueError("The list is empty")
    
    nums.sort()
    n = len(nums)
        
    
    return  (nums[(n-1)//2]+nums[n//2]) /2.0

# Example usage
if __name__ == "__main__":
    nums = [3, 1, 4, 2, 5]
    result = find_median(nums)
    print(f"The median of the list is: {result}")  # Output: 3
