def unique_paths_with_obstacles(obstacleGrid):
    """
    Returns the number of unique paths from top-left to bottom-right in a grid with obstacles.
    Uses O(n) space.
    """
    if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * n
    dp[0] = 1

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[j] = 0
            else:
                if j > 0:
                    dp[j] += dp[j-1]
    return dp[-1]


def test_unique_paths_with_obstacles():
    # Example 1
    g1 = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    assert unique_paths_with_obstacles(g1) == 2

    # Obstacle at start
    g2 = [
        [1,0]
    ]
    assert unique_paths_with_obstacles(g2) == 0

    # Obstacle at end
    g3 = [
        [0,0,0],
        [0,1,0],
        [0,0,1]
    ]
    assert unique_paths_with_obstacles(g3) == 0

    # No obstacles
    g4 = [
        [0,0],
        [0,0]
    ]
    assert unique_paths_with_obstacles(g4) == 2

    # All blocked except start and end not connected
    g5 = [
        [0,1],
        [1,0]
    ]
    assert unique_paths_with_obstacles(g5) == 0

    # Single cell open
    g6 = [
        [0]
    ]
    assert unique_paths_with_obstacles(g6) == 1

    # Single cell blocked
    g7 = [
        [1]
    ]
    assert unique_paths_with_obstacles(g7) == 0

    print("All tests passed!")

if __name__ == "__main__":
    test_unique_paths_with_obstacles()

