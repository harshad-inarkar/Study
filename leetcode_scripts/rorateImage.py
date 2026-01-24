def rotate(matrix):
    """
    Rotates the given n x n 2D matrix by 90 degrees clockwise in-place.
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()

# Test cases
def test_rotate():
    mat1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    rotate(mat1)
    assert mat1 == [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]

    mat2 = [
        [5, 1, 9,11],
        [2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]
    rotate(mat2)
    assert mat2 == [
        [15,13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7,10,11]
    ]

    mat3 = [[1]]
    rotate(mat3)
    assert mat3 == [[1]]

    mat4 = [
        [1,2],
        [3,4]
    ]
    rotate(mat4)
    assert mat4 == [
        [3,1],
        [4,2]
    ]

    print("All test cases passed!")

test_rotate()
