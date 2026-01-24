def max_points_on_line(points):
    """
    Given a list of points (as [x, y]), returns the maximum number of points that lie on a straight line.
    """
    if not points:
        return 0
    from collections import defaultdict
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    max_points = 1
    n = len(points)
    for i in range(n):
        slopes = defaultdict(int)
        duplicates = 0
        cur_max = 0
        x1, y1 = points[i]
        for j in range(i+1, n):
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1
            if dx == 0 and dy == 0:
                duplicates += 1
                continue
            g = gcd(dx, dy)
            if g != 0:
                dx //= g
                dy //= g
            # To handle sign, always keep dx positive
            if dx < 0:
                dx, dy = -dx, -dy
            elif dx == 0:
                dy = 1
            elif dy == 0:
                dx = 1
            slopes[(dx, dy)] += 1
            cur_max = max(cur_max, slopes[(dx, dy)])
        max_points = max(max_points, cur_max + duplicates + 1)
    return max_points

# Example usage and tests
def test_max_points_on_line():
    assert max_points_on_line([[1,1],[2,2],[3,3]]) == 3
    assert max_points_on_line([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4
    assert max_points_on_line([[0,0]]) == 1
    assert max_points_on_line([[0,0],[0,0],[0,0]]) == 3
    assert max_points_on_line([[1,1],[2,2],[3,3],[4,4],[5,5],[1,2],[2,3],[3,4]]) == 5
    assert max_points_on_line([]) == 0
    assert max_points_on_line([[0,0],[1,1],[1,-1]]) == 2
    print("All tests passed for max_points_on_line.")

if __name__ == "__main__":
    test_max_points_on_line()
