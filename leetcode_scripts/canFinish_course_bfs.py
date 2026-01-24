def canFinish(numCourses, prerequisites):
    """
    Determines if you can finish all courses given the prerequisites.
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
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
    visited = 0

    while queue:
        node = queue.popleft()
        visited += 1
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return visited == numCourses

# Tests
def test_canFinish():
    # Test 1: Simple acyclic
    assert canFinish(2, [[1,0]]) == True

    # Test 2: Simple cycle
    assert canFinish(2, [[1,0],[0,1]]) == False

    # Test 3: No prerequisites
    assert canFinish(3, []) == True

    # Test 4: Larger acyclic
    assert canFinish(4, [[1,0],[2,1],[3,2]]) == True

    # Test 5: Larger cycle
    assert canFinish(4, [[1,0],[2,1],[3,2],[1,3]]) == False

    # Test 6: Disconnected graph, one cycle
    assert canFinish(5, [[1,0],[2,1],[3,4],[4,3]]) == False

    # Test 7: Disconnected graph, no cycle
    assert canFinish(5, [[1,0],[2,1],[3,4]]) == True

    print("All tests passed.")

if __name__ == "__main__":
    test_canFinish()
