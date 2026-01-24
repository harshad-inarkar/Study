def search_matrix(matrix, target):
    """
    Searches for a target value in a 2D matrix.
    The matrix has the following properties:
      - Integers in each row are sorted from left to right.
      - The first integer of each row is greater than the last integer of the previous row.
    Returns True if target is found, else False.
    """
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Tests
def test_search_matrix():
    # Test 1: Target present
    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert search_matrix(matrix1, 3) == True
    assert search_matrix(matrix1, 16) == True
    assert search_matrix(matrix1, 60) == True

    # Test 2: Target not present
    assert search_matrix(matrix1, 13) == False
    assert search_matrix(matrix1, 0) == False
    assert search_matrix(matrix1, 61) == False

    # Test 3: Empty matrix
    assert search_matrix([], 1) == False
    assert search_matrix([[]], 1) == False

    # Test 4: Single row
    matrix2 = [[1, 2, 3, 4, 5]]
    assert search_matrix(matrix2, 3) == True
    assert search_matrix(matrix2, 6) == False

    # Test 5: Single column
    matrix3 = [[1], [3], [5], [7]]
    assert search_matrix(matrix3, 5) == True
    assert search_matrix(matrix3, 2) == False

    # Test 6: Single element
    matrix4 = [[7]]
    assert search_matrix(matrix4, 7) == True
    assert search_matrix(matrix4, 8) == False

    print("All test cases passed!")

test_search_matrix()
