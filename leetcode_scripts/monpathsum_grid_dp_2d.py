def min_path_sum(grid):
    """
    Returns the minimum path sum from top-left to bottom-right in a grid.
    You can only move either down or right at any point in time.
    """
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[m-1][n-1]

def test_min_path_sum():
    assert min_path_sum([[1,3,1],[1,5,1],[4,2,1]]) == 7  # 1→3→1→1→1
    assert min_path_sum([[1,2,3],[4,5,6]]) == 12         # 1→2→3→6
    assert min_path_sum([[5]]) == 5                      # Single element grid
    assert min_path_sum([[1,1],[1,1]]) == 3              # All ones
    assert min_path_sum([[1,2],[1,1]]) == 3              # 1→1→1
    assert min_path_sum([[0]]) == 0                      # Single zero
    assert min_path_sum([]) == 0                         # Empty grid
    assert min_path_sum([[]]) == 0                       # Empty grid row
    print("All tests passed!")

if __name__ == "__main__":
    test_min_path_sum()
