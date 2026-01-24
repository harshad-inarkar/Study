def spiralOrder(matrix):
    """
    Returns all elements of the matrix in spiral order.
    """
    if not matrix or not matrix[0]:
        return []
    res = []
    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix[0])-1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for j in range(left, right+1):
            res.append(matrix[top][j])
        top += 1

        # Traverse downwards
        for i in range(top, bottom+1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left
            for j in range(right, left-1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1

        if left <= right:
            # Traverse upwards
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1

    return res

# Test cases
def test_spiralOrder():
    assert spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    assert spiralOrder([[1]]) == [1]
    assert spiralOrder([[1,2],[3,4]]) == [1,2,4,3]
    assert spiralOrder([]) == []
    assert spiralOrder([[1],[2],[3],[4]]) == [1,2,3,4]
    assert spiralOrder([[1,2,3,4]]) == [1,2,3,4]
    print("All test cases passed!")

test_spiralOrder()
