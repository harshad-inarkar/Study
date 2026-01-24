def majority_element_n3(nums: list[int]) -> list[int]:
    """
    Find all elements that appear more than n/3 times in the array.
    Uses Boyer-Moore Voting Algorithm extension for two candidates.
    
    Parameters:
        nums: List[int] - Input array
    Returns:
        List[int] - List of majority elements (at most 2 elements)
    """
    if not nums:
        return []
        
    # Initialize two candidates and their counts
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0
    
    # First pass: Find two potential candidates
    for i in range(len(nums)):
        if count1 == 0:
            candidate1=nums[i]
            count1=1
        elif count2 == 0:
            candidate2=nums[i]
            count2=1
        elif nums[i] == candidate1:
            count1+=1
        elif nums[i] == candidate2:
            count2+=1
        else:
            count1-=1
            count2-=1

    result = []
    for cand in [candidate1,candidate2]:
        if nums.count(cand) > len(nums) // 3:
            result.append(cand)




        

  
        
    return result

# Example usage
if __name__ == "__main__":
    nums = [3, 2, 3, 2]
    result = majority_element_n3(nums)
    print(f"Majority elements (n/3): {result}")  # Output: [3]
