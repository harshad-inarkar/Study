def calcEquation(equations, values, queries):
    """
    Given a list of equations like A / B = k, return the answers to the queries.
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    from collections import defaultdict, deque

    # Build the graph
    graph = defaultdict(dict)
    for (a, b), val in zip(equations, values):
        graph[a][b] = val
        graph[b][a] = 1.0 / val

    def bfs(start, end):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        visited = set()
        queue = deque([(start, 1.0)])
        while queue:
            curr, prod = queue.popleft()
            if curr == end:
                return prod
            visited.add(curr)
            for neighbor, value in graph[curr].items():
                if neighbor not in visited:
                    queue.append((neighbor, prod * value))
        return -1.0

    results = []
    for a, b in queries:
        results.append(bfs(a, b))
    return results

# Tests
def test_calcEquation():
    # Test 1: Example from Leetcode
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    expected = [6.0,0.5,-1.0,1.0,-1.0]
    result = calcEquation(equations, values, queries)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5, f"Test 1 failed: got {result}, expected {expected}"

    # Test 2: Disconnected variables
    equations = [["a","b"],["c","d"]]
    values = [1.5,2.5]
    queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    expected = [1.5, 1/1.5, -1.0, -1.0]
    result = calcEquation(equations, values, queries)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5, f"Test 2 failed: got {result}, expected {expected}"

    # Test 3: Self division
    equations = [["a","b"]]
    values = [4.0]
    queries = [["a","a"],["b","b"],["a","b"],["b","a"]]
    expected = [1.0,1.0,4.0,0.25]
    result = calcEquation(equations, values, queries)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5, f"Test 3 failed: got {result}, expected {expected}"

    # Test 4: Chain
    equations = [["a","b"],["b","c"],["c","d"]]
    values = [2.0,3.0,4.0]
    queries = [["a","d"],["d","a"],["b","d"],["d","b"]]
    expected = [24.0,1/24.0,12.0,1/12.0]
    result = calcEquation(equations, values, queries)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-5, f"Test 4 failed: got {result}, expected {expected}"

    print("All tests passed.")

if __name__ == "__main__":
    test_calcEquation()
