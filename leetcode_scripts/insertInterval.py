def insert(intervals, newInterval):
    """
    Inserts a new interval into a list of non-overlapping intervals sorted by start time,
    merging if necessary.
    Args:
        intervals (List[List[int]]): List of intervals [start, end]
        newInterval (List[int]): The interval to insert
    Returns:
        List[List[int]]: Updated list of merged intervals
    """
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    # Add the rest of the intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

# Tests
def test_insert():
    assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    assert insert([], [5,7]) == [[5,7]]
    assert insert([[1,5]], [2,3]) == [[1,5]]
    assert insert([[1,5]], [2,7]) == [[1,7]]
    assert insert([[1,5]], [6,8]) == [[1,5],[6,8]]
    assert insert([[3,5],[12,15]], [6,6]) == [[3,5],[6,6],[12,15]]
    print("All tests passed!")

test_insert()
