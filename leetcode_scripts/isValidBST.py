class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    """
    Returns True if the binary tree is a valid binary search tree (BST), False otherwise.
    """
    def helper(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)
    return helper(root, float('-inf'), float('inf'))

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
def test_isValidBST():
    # Test 1: Valid BST
    #      2
    #     / \
    #    1   3
    root = build_tree([2,1,3])
    assert isValidBST(root) == True

    # Test 2: Invalid BST
    #      5
    #     / \
    #    1   4
    #       / \
    #      3   6
    root = build_tree([5,1,4,None,None,3,6])
    assert isValidBST(root) == False

    # Test 3: Single node
    root = build_tree([1])
    assert isValidBST(root) == True

    # Test 4: Empty tree
    root = build_tree([])
    assert isValidBST(root) == True

    # Test 5: Invalid BST with duplicate values
    root = build_tree([2,2,2])
    assert isValidBST(root) == False

    # Test 6: Valid BST with negative values
    root = build_tree([0,-1])
    assert isValidBST(root) == True

    # Test 7: Invalid BST deeper violation
    #      10
    #     /  \
    #    5    15
    #        /  \
    #       6    20
    root = build_tree([10,5,15,None,None,6,20])
    assert isValidBST(root) == False

    print("All tests passed.")

if __name__ == "__main__":
    test_isValidBST()
