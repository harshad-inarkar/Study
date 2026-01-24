
def candy_one_pass(ratings: list[int]) -> int:
    """
    Distribute candies to children based on their ratings using a one-pass solution.
    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    
    Parameters:
        ratings: List[int] - Array of children's ratings
    Returns:
        int - Minimum number of candies needed
    """
    n = len(ratings)
    if n == 0:
        return 0

    candies = 1
    up = down = peak = 0

    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            up += 1
            peak = up
            down = 0
            candies += 1 + up
        elif ratings[i] < ratings[i-1]:
            up = 0
            down += 1
            candies += down
            if peak < down:
                candies +=1
        else:
            up = down = peak = 0
            candies += 1

    return candies

# Example usage
if __name__ == "__main__":
    ratings = [1, 2, 3,6,5,4,3,2,1,0]
    result = candy_one_pass(ratings)
    print(f"Minimum candies needed (one pass): {result}")  # Output: 5




