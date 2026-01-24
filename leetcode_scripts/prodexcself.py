def productExceptSelf(nums: list[int]) -> list[int]:
    """
    Calculate the product of all elements except self for each element in the array.
    Must be done in O(n) time without using division operation.
    
    Parameters:
        nums: List[int] - Input array of integers
    Returns:
        List[int] - Array where each element is product of all elements except itself
    """
    answer = [1] * len(nums)

    for i in range(1,len(nums)):
        answer[i] = answer[i-1] * nums[i-1]
    
    rp = 1
    for i in range(len(nums)-1,-1,-1):
        answer[i] *= rp
        rp*=nums[i]


    return answer 

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    result = productExceptSelf(nums)
    print(result)  # Output: [24, 12, 8, 6]
