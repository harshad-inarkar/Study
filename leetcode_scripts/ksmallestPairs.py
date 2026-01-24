def kSmallestPairs(nums1, nums2, k):
    """
    Find the k pairs (u,v) with the smallest sums, where u from nums1 and v from nums2.
    """
    import heapq
    if not nums1 or not nums2 or k == 0:
        return []
    min_heap = [(nums1[0] + nums2[0], 0, 0)]
    res = []
    n1= len(nums1)-1
    n2= len(nums2)-1
    
    # Only need to consider first k elements from nums1 (if nums2 is not empty)
    
 
    while min_heap and k:
        total, i, j = heapq.heappop(min_heap)
        res.append([nums1[i], nums2[j]])
        k-=1

        if i < n1 and j==0:
            heapq.heappush(min_heap, (nums1[i+1] + nums2[j], i+1, j))

        if j < n2:
            heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
            
    return res

# Unit tests
def test_kSmallestPairs():
    assert kSmallestPairs([1,7,11], [2,4,6], 3) == [[1,2],[1,4],[1,6]]
    assert kSmallestPairs([1,1,2], [1,2,3], 2) == [[1,1],[1,1]]
    assert kSmallestPairs([1,2], [3], 3) == [[1,3],[2,3]]
    assert kSmallestPairs([], [1,2], 3) == []
    assert kSmallestPairs([1,2], [], 3) == []
    assert kSmallestPairs([1,2], [3,4], 0) == []
    assert kSmallestPairs([1,2], [3,4], 10) == [[1,3],[1,4],[2,3],[2,4]]
    print("All test cases passed!")

test_kSmallestPairs()
