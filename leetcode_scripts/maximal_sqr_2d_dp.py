def maximal_square(matrix):
    """
    Given a 2D binary matrix filled with '0's and '1's,
    finds the largest square containing only 1's and returns its area.
    """
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0]*(n+1) for _ in range(m+1)]
    max_side = 0
    for i in range(1,m+1):
        for j in range(1, n+1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = min(
                    dp[i-1][j],
                    dp[i][j-1],
                    dp[i-1][j-1]
                ) + 1
                max_side = max(max_side, dp[i][j])
    return max_side * max_side

def test_maximal_square():
    m1 = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    assert maximal_square(m1) == 4  # 2x2 square

    m2 = [
        ["0","1"],
        ["1","0"]
    ]
    assert maximal_square(m2) == 1  # single element is max

    m3 = [
        ["0"]
    ]
    assert maximal_square(m3) == 0  # all zero

    m4 = [
        ["1","1","1","1"],
        ["1","1","1","1"],
        ["1","1","1","1"]
    ]
    assert maximal_square(m4) == 9  # 3x3 square

    m5 = []
    assert maximal_square(m5) == 0

    m6 = [["1"]]
    assert maximal_square(m6) == 1

    m7 = [
        ["0","0","1","0"],
        ["1","1","1","1"],
        ["1","1","1","1"],
        ["1","1","1","0"]
    ]
    assert maximal_square(m7) == 9

    print("All tests passed for maximal_square.")

if __name__ == "__main__":
    test_maximal_square()
