def majority_element(nums: list[int]) -> int:
    """
    Find the majority element in the array that appears more than n/2 times.
    Uses Boyer-Moore Voting Algorithm.
    
    Parameters:
        nums: List[int] - Input array
    Returns:
        int - The majority element
    """
    count = 0
    candidate = None
    
    # Find candidate for majority element
    for i in range(len(nums)):
        if count == 0:
            candidate = nums[i]
            
        count += 1 if nums[i] == candidate else -1
            
    return candidate

# Example usage
if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = majority_element(nums)
    print(f"Majority element: {result}")  # Output: 2
