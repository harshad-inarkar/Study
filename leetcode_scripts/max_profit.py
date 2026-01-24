def max_profit(prices: list[int]) -> int:
    """
    Calculate the maximum profit from buying and selling stocks.
    You can buy and sell only once.
    
    Parameters:
        prices: List[int] - Array of stock prices
    Returns:
        int - Maximum possible profit
    """

    max_profit = 0

    if prices:
        buy = prices[0]
        for price in prices:
                # Update the minimum price so far

            if price < buy:
                buy = price
            elif (price - buy) > max_profit:
                max_profit = price - buy

    return max_profit

# Example usage
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    result = max_profit(prices)
    print(f"Maximum profit: {result}")  # Output: 5 (buy at 1, sell at 6)
