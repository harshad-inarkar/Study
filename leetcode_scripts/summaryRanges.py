def summaryRanges(nums):
    """
    Given a sorted integer array without duplicates, returns the smallest sorted list of ranges that cover all the numbers in the array exactly.
    Each range [a,b] is represented as:
      - "a->b" if a != b
      - "a" if a == b
    """
    ranges = []
    if not nums:
        return ranges

    start = end = nums[0]
    for n in nums[1:]:
        if n == end + 1:
            end = n
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{end}")
            start = end = n
    # Add the last range
    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}->{end}")
    return ranges

# Tests
def test_summaryRanges():
    assert summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"]
    assert summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]
    assert summaryRanges([]) == []
    assert summaryRanges([1]) == ["1"]
    assert summaryRanges([1,2]) == ["1->2"]
    assert summaryRanges([-1,0,1,2,6,7,8,10]) == ["-1->2","6->8","10"]
    print("All tests passed!")

test_summaryRanges()
