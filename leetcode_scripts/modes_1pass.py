
from collections import defaultdict

def mode_single_pass(nums: list[int]) -> list[int]:
    """
    Calculate the mode of a list of numbers in a single pass.
    
    Parameters:
        nums: List[int] - Input array of integers
    Returns:
        int - The mode of the list
    """
    if not nums:
        raise ValueError("The list is empty")
    
    frequency =defaultdict(int)
    modes = []
    max_count = 0
    
    for num in nums:
        frequency[num] +=1
        
        if frequency[num] > max_count:
            max_count = frequency[num]
            modes = [num]
        elif frequency[num] == max_count and num not in modes:
            modes.append(num)
    
    return modes

# Example usage
if __name__ == "__main__":
    nums = [1,4,3,4,5,5]
    result = mode_single_pass(nums)
    print(f"The mode of the list is: {result}")  # Output: 3
