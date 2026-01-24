def combine(n, k):
    """
    Return all possible combinations of k numbers out of 1 ... n.
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    res = []
    path = [0]*k
    def backtrack(start, pathlen):
        if pathlen == k:
            res.append(path[:])
            return
        
        # prune logic
        max_start = n - (k -pathlen) +1
        for i in range(start, max_start+1):
            path[pathlen] = i
            backtrack(i+1, pathlen+1)
        
    backtrack(1, 0)
    return res

# Tests
def test_combine():
    assert sorted(combine(4,2)) == sorted([
        [1,2],[1,3],[1,4],[2,3],[2,4],[3,4]
    ]), "Test 1 failed"
    assert combine(1,1) == [[1]], "Test 2 failed"
    assert combine(3,1) == [[1],[2],[3]], "Test 3 failed"
    assert combine(3,3) == [[1,2,3]], "Test 4 failed"
    assert combine(3,0) == [[]], "Test 5 failed"
    assert combine(0,0) == [[]], "Test 6 failed"
    print("All tests passed.")

if __name__ == "__main__":
    test_combine()
