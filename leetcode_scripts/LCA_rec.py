class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    """
    Finds the lowest common ancestor (LCA) of two nodes in a binary tree.
    Assumes all TreeNode values are unique and both p and q are present in the tree.
    """
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

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

# Helper to find node by value
def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)

# Tests
def test_lowestCommonAncestor():
    # Test 1: Example tree
    #      3
    #     / \
    #    5   1
    #   / \ / \
    #  6  2 0  8
    #    / \
    #   7   4
    root = build_tree([3,5,1,6,2,0,8,None,None,7,4])
    p = find_node(root, 5)
    q = find_node(root, 1)
    lca = lowestCommonAncestor(root, p, q)
    assert lca.val == 3

    p = find_node(root, 5)
    q = find_node(root, 4)
    lca = lowestCommonAncestor(root, p, q)
    assert lca.val == 5

    p = find_node(root, 6)
    q = find_node(root, 4)
    lca = lowestCommonAncestor(root, p, q)
    assert lca.val == 5

    p = find_node(root, 7)
    q = find_node(root, 8)
    lca = lowestCommonAncestor(root, p, q)
    assert lca.val == 3

    # Test 2: Single node tree
    root = build_tree([1])
    p = find_node(root, 1)
    q = find_node(root, 1)
    lca = lowestCommonAncestor(root, p, q)
    assert lca.val == 1

    # Test 3: Left-skewed tree
    #    1
    #   /
    #  2
    # /
    #3
    root = build_tree([1,2,None,3])
    p = find_node(root, 2)
    q = find_node(root, 3)
    lca = lowestCommonAncestor(root, p, q)
    assert lca.val == 2

    # Test 4: Right-skewed tree
    # 1
    #  \
    #   2
    #    \
    #     3
    root = build_tree([1,None,2,None,3])
    p = find_node(root, 1)
    q = find_node(root, 3)
    lca = lowestCommonAncestor(root, p, q)
    assert lca.val == 1

    print("All tests passed.")

if __name__ == "__main__":
    test_lowestCommonAncestor()
