def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    """
    Determine if you can travel around the circuit once in the clockwise direction.
    If you can, return the starting gas station's index, otherwise return -1.
    
    Parameters:
        gas: List[int] - Amount of gas available at each station
        cost: List[int] - Cost to travel from station i to station i+1
    Returns:
        int - Starting index if possible, -1 otherwise
    """
    if sum(gas) < sum(cost):
        return -1
        
    total = 0
    start = 0
    
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            total = 0
            start = i + 1
            
    return start

# Example usage
if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    result = canCompleteCircuit(gas, cost)
    print(f"Starting station: {result}")  # Output: 3
