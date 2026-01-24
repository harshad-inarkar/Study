class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    """
    Computes the maximum depth of a binary tree using an iterative (non-recursive) approach.
    Args:
        root (TreeNode): The root of the binary tree.
    Returns:
        int: The maximum depth.
    """
    if not root:
        return 0
    stack = [(root, 1)]
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        if node:
            max_depth = max(max_depth, depth)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
    return max_depth

# Helper function to build a tree from list (level order)
def list_to_tree(lst):
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
def test_maxDepth():
    # Test 1: Empty tree
    assert maxDepth(None) == 0

    # Test 2: Single node
    t2 = TreeNode(1)
    assert maxDepth(t2) == 1

    # Test 3: Complete binary tree
    t3 = list_to_tree([3,9,20,None,None,15,7])
    assert maxDepth(t3) == 3

    # Test 4: Skewed left
    t4 = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert maxDepth(t4) == 3

    # Test 5: Skewed right
    t5 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert maxDepth(t5) == 3

    # Test 6: Larger tree
    t6 = list_to_tree([1,2,2,3,3,None,None,4,4])
    assert maxDepth(t6) == 4

    print("All tests passed!")

test_maxDepth()
