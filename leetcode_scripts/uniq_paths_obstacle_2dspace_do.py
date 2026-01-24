def unique_paths_with_obstacles(obstacleGrid):
    """
    Returns the number of unique paths from top-left to bottom-right in a grid with obstacles.
    grid[i][j] == 1 means obstacle, 0 means open cell.
    Can only move right or down.
    """
    if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])


    dp = [[0] * n for _ in range(m)]

    dp[0][0] = 1

    for j in range(1,n):
        dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j-1]
    
    for i in range(1,m):
        dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i-1][0]


    for i in range(1,m):
        for j in range(1,n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]


def test_unique_paths_with_obstacles():
    # Example 1
    g1 = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    assert unique_paths_with_obstacles(g1) == 2  # Only two ways

    # Example 2: Obstacle at start
    g2 = [
        [1,0]
    ]
    assert unique_paths_with_obstacles(g2) == 0

    # Example 3: Obstacle at finish
    g3 = [
        [0,0,0],
        [0,1,0],
        [0,0,1]
    ]
    assert unique_paths_with_obstacles(g3) == 0

    # Example 4: No obstacles (regular unique path)
    g4 = [
        [0,0],
        [0,0]
    ]
    assert unique_paths_with_obstacles(g4) == 2

    # Example 5: All blocked
    g5 = [
        [0,1],
        [1,0]
    ]
    assert unique_paths_with_obstacles(g5) == 0

    # Example 6: Single cell open
    g6 = [
        [0]
    ]
    assert unique_paths_with_obstacles(g6) == 1

    # Example 7: Single cell blocked
    g7 = [
        [1]
    ]
    assert unique_paths_with_obstacles(g7) == 0

    print("All tests passed!")

if __name__ == "__main__":
    test_unique_paths_with_obstacles()

