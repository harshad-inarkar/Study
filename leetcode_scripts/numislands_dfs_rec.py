def numIslands(grid):
    """
    Given a 2D grid map of '1's (land) and '0's (water), count the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # Mark as visited
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count

# Tests
def test_numIslands():
    # Test 1: Example case
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert numIslands([row[:] for row in grid1]) == 1

    # Test 2: Multiple islands
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert numIslands([row[:] for row in grid2]) == 3

    # Test 3: All water
    grid3 = [
        ["0","0","0"],
        ["0","0","0"]
    ]
    assert numIslands([row[:] for row in grid3]) == 0

    # Test 4: All land
    grid4 = [
        ["1","1"],
        ["1","1"]
    ]
    assert numIslands([row[:] for row in grid4]) == 1

    # Test 5: Single cell island
    grid5 = [
        ["1"]
    ]
    assert numIslands([row[:] for row in grid5]) == 1

    # Test 6: Single cell water
    grid6 = [
        ["0"]
    ]
    assert numIslands([row[:] for row in grid6]) == 0

    # Test 7: Empty grid
    grid7 = []
    assert numIslands(grid7) == 0

    print("All tests passed.")

if __name__ == "__main__":
    test_numIslands()
