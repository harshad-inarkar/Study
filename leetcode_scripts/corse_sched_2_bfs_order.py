def findOrder(numCourses, prerequisites):
    """
    Returns the order in which you should take courses to finish all courses.
    If it is impossible, returns an empty list.
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    from collections import defaultdict, deque

    # Build the adjacency list and in-degree array
    adj = defaultdict(list)
    in_degree = [0] * numCourses
    for dest, src in prerequisites:
        adj[src].append(dest)
        in_degree[dest] += 1

    # Queue for nodes with in-degree 0
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) == numCourses:
        return order
    else:
        return []

# Tests
def test_findOrder():
    # Test 1: Simple acyclic
    result = findOrder(2, [[1,0]])
    assert result == [0,1] or result == [1,0] and [1,0] == [0,1], f"Test 1 failed: got {result}"

    # Test 2: Simple cycle
    result = findOrder(2, [[1,0],[0,1]])
    assert result == [], f"Test 2 failed: got {result}"

    # Test 3: No prerequisites
    result = findOrder(3, [])
    assert set(result) == {0,1,2} and len(result) == 3, f"Test 3 failed: got {result}"

    # Test 4: Larger acyclic
    result = findOrder(4, [[1,0],[2,1],[3,2]])
    assert result == [0,1,2,3], f"Test 4 failed: got {result}"

    # Test 5: Larger cycle
    result = findOrder(4, [[1,0],[2,1],[3,2],[1,3]])
    assert result == [], f"Test 5 failed: got {result}"

    # Test 6: Disconnected graph, one cycle
    result = findOrder(5, [[1,0],[2,1],[3,4],[4,3]])
    assert result == [], f"Test 6 failed: got {result}"

    # Test 7: Disconnected graph, no cycle
    result = findOrder(5, [[1,0],[2,1],[3,4]])
    assert set(result) == {0,1,2,3,4} and len(result) == 5, f"Test 7 failed: got {result}"

    print("All tests passed.")

if __name__ == "__main__":
    test_findOrder()
