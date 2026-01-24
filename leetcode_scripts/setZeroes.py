def setZeroes(matrix):
    """
    Given an m x n matrix, if an element is 0, set its entire row and column to 0 in-place.
    """
    if not matrix or not matrix[0]:
        return
    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # Use first row and column as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set zeroes based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Set first row to zero if needed
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    # Set first column to zero if needed
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

# Test cases
def test_setZeroes():
    mat1 = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
    setZeroes(mat1)
    assert mat1 == [
        [1,0,1],
        [0,0,0],
        [1,0,1]
    ]

    mat2 = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ]
    setZeroes(mat2)
    assert mat2 == [
        [0,0,0,0],
        [0,4,5,0],
        [0,3,1,0]
    ]

    mat3 = [
        [1,2,3,4],
        [5,6,7,8],
        [0,10,11,12]
    ]
    setZeroes(mat3)
    assert mat3 == [
        [0,2,3,4],
        [0,6,7,8],
        [0,0,0,0]
    ]

    mat4 = [
        [0]
    ]
    setZeroes(mat4)
    assert mat4 == [
        [0]
    ]

    mat5 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    setZeroes(mat5)
    assert mat5 == [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    print("All test cases passed!")

test_setZeroes()
