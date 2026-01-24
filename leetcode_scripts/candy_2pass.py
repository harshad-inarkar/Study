def candy(ratings: list[int]) -> int:
    """
    Distribute candies to children based on their ratings.
    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    
    Parameters:
        ratings: List[int] - Array of children's ratings
    Returns:
        int - Minimum number of candies needed
    """
    n = len(ratings)
    candies = [1] * n
    
    # Left to right pass
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
            
    # Right to left pass
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
            
    return sum(candies)

# Example usage
if __name__ == "__main__":
    ratings = [1, 0, 2]
    result = candy(ratings)
    print(f"Minimum candies needed: {result}")  # Output: 5
