def max_profit_2(prices: list[int]) -> int:
    """
    Calculate the maximum profit from buying and selling stocks.
    You can buy and sell multiple times, but must sell before buying again.
    
    Parameters:
        prices: List[int] - Array of stock prices
    Returns:
        int - Maximum possible profit
    """
    return sum(
            prices[i] - prices[i - 1]
            for i in range(1, len(prices))
            if prices[i] > prices[i - 1]
        )

# Example usage
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    result = max_profit_2(prices)
    print(f"Maximum profit: {result}")  # Output: 7 (buy at 1, sell at 5; buy at 3, sell at 6)
