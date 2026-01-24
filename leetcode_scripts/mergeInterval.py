def merge(intervals):
    """
    Given a collection of intervals, merge all overlapping intervals.
    Args:
        intervals (List[List[int]]): List of intervals [start, end]
    Returns:
        List[List[int]]: Merged intervals
    """
    if not intervals:
        return []
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            # Overlap, merge
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged

# Tests
def test_merge():
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4],[4,5]]) == [[1,5]]
    assert merge([]) == []
    assert merge([[1,4]]) == [[1,4]]
    assert merge([[1,4],[0,2],[3,5]]) == [[0,5]]
    assert merge([[1,4],[2,3]]) == [[1,4]]
    assert merge([[1,10],[2,6],[8,10],[15,18]]) == [[1,10],[15,18]]
    print("All tests passed!")

test_merge()
