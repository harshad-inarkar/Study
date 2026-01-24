def jump_game_2(nums: list[int]) -> int:
    """
    Find the minimum number of jumps needed to reach the last index.
    Each element represents the maximum jump length from that position.
    
    Parameters:
        nums: List[int] - Array of jump lengths
    Returns:
        int - Minimum number of jumps required
    """
    max_reach, end, jumps = 0,0,0

    for i,num in enumerate(nums[:-1]):            
        if max_reach < i + num:
            max_reach = i + num

        if i == end:
            jumps+=1
            end = max_reach

            if end >= len(nums) -1:
                break
    
    if end < len(nums) -1:
        jumps = -1

    return jumps

# Example usage
if __name__ == "__main__":
    nums = [1, 1, 1, 1, 4]
    result = jump_game_2(nums)
    print(f"Minimum jumps required: {result}")  # Output: 2
