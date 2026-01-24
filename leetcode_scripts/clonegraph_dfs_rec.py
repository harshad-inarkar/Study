class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraphDFS(node):
    """
    Clones a connected undirected graph using DFS.
    :type node: Node
    :rtype: Node
    """
    def dfs(curr):
        if not curr:
            return None
        if curr in old_to_new:
            return old_to_new[curr]
        copy = Node(curr.val)
        old_to_new[curr] = copy
        for neighbor in curr.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy

    old_to_new = {}
    return dfs(node)

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
def test_cloneGraphDFS():
    # Test 1: Simple 4-node cycle
    adj1 = [[2,4],[1,3],[2,4],[1,3]]
    node1 = build_graph(adj1)
    clone1 = cloneGraphDFS(node1)
    assert graph_to_adj_list(clone1) == adj1

    # Test 2: Single node, no neighbors
    adj2 = [[]]
    node2 = build_graph(adj2)
    clone2 = cloneGraphDFS(node2)
    assert graph_to_adj_list(clone2) == adj2

    # Test 3: Two nodes, one edge
    adj3 = [[2],[1]]
    node3 = build_graph(adj3)
    clone3 = cloneGraphDFS(node3)
    assert graph_to_adj_list(clone3) == adj3

    # Test 4: Empty graph
    node4 = build_graph([])
    clone4 = cloneGraphDFS(node4)
    assert clone4 is None

    print("All DFS cloneGraph tests passed.")

if __name__ == "__main__":
    test_cloneGraphDFS()
