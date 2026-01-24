class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root):
    """
    Returns the minimum absolute difference between values of any two nodes in a BST.
    """
    prev = [None]
    min_diff = [float('inf')]

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        if prev[0] is not None:
            min_diff[0] = min(min_diff[0], abs(node.val - prev[0]))
        prev[0] = node.val
        inorder(node.right)

    inorder(root)
    return min_diff[0]

# Helper function to build BST from list (level order, None for missing nodes)
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
def test_getMinimumDifference():
    # Test 1: Example BST
    #      4
    #     / \
    #    2   6
    #   / \
    #  1   3
    root = build_tree([4,2,6,1,3])
    assert getMinimumDifference(root) == 1

    # Test 2: BST with only two nodes
    root = build_tree([1,None,3])
    assert getMinimumDifference(root) == 2

    # Test 3: BST with negative values
    root = build_tree([5,3,8,1,None,7,10])
    assert getMinimumDifference(root) == 1

    # Test 4: BST with consecutive values
    root = build_tree([10,5,15,3,7,13,18])
    assert getMinimumDifference(root) == 2

    # Test 5: Single node
    root = build_tree([1])
    assert getMinimumDifference(root) == float('inf')

    print("All tests passed.")

if __name__ == "__main__":
    test_getMinimumDifference()
