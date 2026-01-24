def maxArea(height):
    """
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
    Find two lines, which together with the x-axis forms a container, such that the container contains the most water.
    """
    l,r, maxarea = 0, len(height) -1,0

    while l < r:
        w = r - l
        if height[l]< height[r]:
            h = height[l]
            l+=1
        else:
            h = height[r]
            r-=1

        maxarea = max(maxarea,h*w)

    return maxarea


# Test cases
def test_maxArea():
    assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert maxArea([1,1]) == 1
    assert maxArea([4,3,2,1,4]) == 16
    assert maxArea([1,2,1]) == 2
    assert maxArea([2,3,10,5,7,8,9]) == 36
    print("All test cases passed!")

test_maxArea()
