class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    """
    Clones a connected undirected graph using BFS.
    :type node: Node
    :rtype: Node
    """
    if not node:
        return None

    old_to_new = {}

    from collections import deque
    queue = deque([node])
    old_to_new[node] = Node(node.val)

    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor not in old_to_new:
                old_to_new[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            old_to_new[curr].neighbors.append(old_to_new[neighbor])

    return old_to_new[node]

# Helper functions for testing
def build_graph(adj_list):
    """
    Builds a graph from an adjacency list.
    adj_list: List[List[int]]
    Returns the reference to the first node.
    """
    if not adj_list:
        return None
    nodes = [Node(i+1) for i in range(len(adj_list))]
    for idx, neighbors in enumerate(adj_list):
        nodes[idx].neighbors = [nodes[n-1] for n in neighbors]
    return nodes[0]

def graph_to_adj_list(node):
    """
    Converts a graph to an adjacency list.
    Returns List[List[int]]
    """
    if not node:
        return []
    from collections import deque
    adj = {}
    queue = deque([node])
    visited = set([node])
    while queue:
        curr = queue.popleft()
        adj[curr.val] = [n.val for n in curr.neighbors]
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    # Return in order of node values
    return [adj[i+1] for i in range(len(adj))]

# Tests
def test_cloneGraph():
    # Test 1: 4-node square
    adj1 = [[2,4],[1,3],[2,4],[1,3]]
    node1 = build_graph(adj1)
    clone1 = cloneGraph(node1)
    assert graph_to_adj_list(clone1) == adj1

    # Test 2: Single node
    adj2 = [[]]
    node2 = build_graph(adj2)
    clone2 = cloneGraph(node2)
    assert graph_to_adj_list(clone2) == adj2

    # Test 3: Two nodes, one edge
    adj3 = [[2],[1]]
    node3 = build_graph(adj3)
    clone3 = cloneGraph(node3)
    assert graph_to_adj_list(clone3) == adj3

    # Test 4: Triangle
    adj4 = [[2,3],[1,3],[1,2]]
    node4 = build_graph(adj4)
    clone4 = cloneGraph(node4)
    assert graph_to_adj_list(clone4) == adj4

    # Test 5: Empty graph
    node5 = build_graph([])
    clone5 = cloneGraph(node5)
    assert clone5 is None

    print("All tests passed.")

if __name__ == "__main__":
    test_cloneGraph()
