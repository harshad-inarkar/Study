class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    """
    Returns True if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
    """
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == targetSum
    return (hasPathSum(root.left, targetSum - root.val) or
            hasPathSum(root.right, targetSum - root.val))

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
def test_hasPathSum():
    # Test 1: Example tree
    #     5
    #    / \
    #   4   8
    #  /   / \
    # 11  13  4
    # / \      \
    #7   2      1
    root = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    assert hasPathSum(root, 22) == True  # 5->4->11->2

    # Test 2: No path sum
    assert hasPathSum(root, 26) == True  # 5->8->13
    assert hasPathSum(root, 18) == True  # 5->8->4->1
    assert hasPathSum(root, 27) == False

    # Test 3: Empty tree
    assert hasPathSum(None, 0) == False

    # Test 4: Single node
    root = build_tree([1])
    assert hasPathSum(root, 1) == True
    assert hasPathSum(root, 2) == False

    # Test 5: Negative values
    root = build_tree([-2,None,-3])
    assert hasPathSum(root, -5) == True

    print("All test cases passed!")

test_hasPathSum()
