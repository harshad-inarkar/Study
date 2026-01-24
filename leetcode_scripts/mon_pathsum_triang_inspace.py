def minimum_total(triangle):
    """
    Given a triangle array, return the minimum path sum from top to bottom.
    Each step, you may move to adjacent numbers on the row below.
    """
    if not triangle:
        return 0
    # Copy the last row as the initial dp
    # Bottom up DP
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]

def test_minimum_total():
    # Basic example
    t1 = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
    assert minimum_total(t1) == 11   # 2+3+5+1

    # Single row
    t2 = [[-10]]
    assert minimum_total(t2) == -10

    # Two rows, positive
    t3 = [
        [1],
        [2,3]
    ]
    assert minimum_total(t3) == 3    # 1+2

    # Two rows, negative
    t4 = [
        [-1],
        [-2,-3]
    ]
    assert minimum_total(t4) == -4   # -1 + -2

    # Empty triangle
    t5 = []
    assert minimum_total(t5) == 0

    # All zeros
    t6 = [
        [0],
        [0,0],
        [0,0,0]
    ]
    assert minimum_total(t6) == 0

    print("All tests passed!")

if __name__ == "__main__":
    test_minimum_total()
