from collections import deque

def numIslandsBFS(grid):
    """
    Given a 2D grid map of '1's (land) and '0's (water), count the number of islands using BFS.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        grid[r][c] = '0'  # Mark as visited
        while queue:
            cr, cc = queue.popleft()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                bfs(r, c)
    return count

# Tests
def test_numIslandsBFS():
    # Test 1: Example case
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert numIslandsBFS([row[:] for row in grid1]) == 1

    # Test 2: Multiple islands
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert numIslandsBFS([row[:] for row in grid2]) == 3

    # Test 3: All water
    grid3 = [
        ["0","0","0"],
        ["0","0","0"]
    ]
    assert numIslandsBFS([row[:] for row in grid3]) == 0

    # Test 4: All land
    grid4 = [
        ["1","1"],
        ["1","1"]
    ]
    assert numIslandsBFS([row[:] for row in grid4]) == 1

    # Test 5: Single cell island
    grid5 = [
        ["1"]
    ]
    assert numIslandsBFS([row[:] for row in grid5]) == 1

    # Test 6: Single cell water
    grid6 = [
        ["0"]
    ]
    assert numIslandsBFS([row[:] for row in grid6]) == 0

    # Test 7: Empty grid
    grid7 = []
    assert numIslandsBFS(grid7) == 0

    print("All tests passed.")

if __name__ == "__main__":
    test_numIslandsBFS()
