def findMinArrowShots(points):
    """
    Given a list of intervals representing the start and end of balloons,
    returns the minimum number of arrows required to burst all balloons.
    Each balloon is represented as [start, end].
    """
    if not points:
        return 0
    # Sort by end coordinate
    points.sort(key=lambda x: x[1])
    arrows = 1
    end = points[0][1]
    for start, finish in points[1:]:
        if start > end:
            arrows += 1
            end = finish
    return arrows

# Tests
def test_findMinArrowShots():
    assert findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2
    assert findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4
    assert findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2
    assert findMinArrowShots([[1,10],[2,3],[4,5],[6,7],[8,9]]) == 1
    assert findMinArrowShots([]) == 0
    assert findMinArrowShots([[1,2]]) == 1
    assert findMinArrowShots([[1,5],[2,6],[3,7],[4,8]]) == 1
    print("All tests passed!")

test_findMinArrowShots()
