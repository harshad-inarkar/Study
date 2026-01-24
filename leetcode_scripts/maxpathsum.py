class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    """
    Returns the maximum path sum in the binary tree.
    A path is any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
    The path must contain at least one node and does not need to go through the root.
    """
    max_sum = [float('-inf')]
    
    def dfs(node):
        if not node:
            return 0
        # Compute max path sum for left and right, ignore negatives
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        # Path passing through this node
        curr_sum = node.val + left + right
        max_sum[0] = max(max_sum[0], curr_sum)
        # Return max path sum starting from this node and extending to one child
        return node.val + max(left, right)
    
    dfs(root)
    return max_sum[0]

# Helper function to build tree from list (level order, None for missing nodes)
def build_tree(lst):
    if not lst:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# Tests
def test_maxPathSum():
    # Test 1: Example tree
    #      1
    #     / \
    #    2   3
    root = build_tree([1,2,3])
    assert maxPathSum(root) == 6  # 2+1+3

    # Test 2: Tree with negatives
    #     -10
    #     /  \
    #    9   20
    #        / \
    #       15  7
    root = build_tree([-10,9,20,None,None,15,7])
    assert maxPathSum(root) == 42  # 15+20+7

    # Test 3: Single node
    root = build_tree([2])
    assert maxPathSum(root) == 2

    # Test 4: All negative nodes
    root = build_tree([-3])
    assert maxPathSum(root) == -3

    # Test 5: More complex tree
    #      5
    #     / \
    #    4   8
    #   /   / \
    # 11  13  4
    # / \      \
    #7   2      1
    root = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    assert maxPathSum(root) == 48  # 7+11+4+5+8+13

    print("All test cases passed!")

test_maxPathSum()
