def can_jump(nums: list[int]) -> bool:
    """
    Determine if you can reach the last index of the array.
    Each element represents the maximum jump length from that position.
    
    Parameters:
        nums: List[int] - Array of jump lengths
    Returns:
        bool - True if last index is reachable, False otherwise
    """
        
    max_reach = 0
    for i, num in enumerate(nums):
        
        if i > max_reach:
            break
        
        if max_reach < i + num:
            max_reach = i + num

    return max_reach >= len(nums)-1


# Example usage
if __name__ == "__main__":
    nums = [2,0,1,2,0,1,1]
    result = can_jump(nums)
    print(f"Can reach last index: {result}")  # Output: True
