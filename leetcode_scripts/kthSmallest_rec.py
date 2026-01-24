class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    """
    Returns the kth smallest element in a BST (1-indexed).
    """
    count = [0]
    result = [None]
    def inorder(node):
        if not node or result[0] is not None:
            return
        inorder(node.left)
        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return
        inorder(node.right)
    inorder(root)
    return result[0]

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
def test_kthSmallest():
    # Test 1: Example BST
    #      3
    #     / \
    #    1   4
    #     \
    #      2
    root = build_tree([3,1,4,None,2])
    assert kthSmallest(root, 1) == 1
    assert kthSmallest(root, 2) == 2
    assert kthSmallest(root, 3) == 3
    assert kthSmallest(root, 4) == 4

    # Test 2: BST with more nodes
    #      5
    #     / \
    #    3   6
    #   / \
    #  2   4
    # /
    #1
    root = build_tree([5,3,6,2,4,None,None,1])
    assert kthSmallest(root, 1) == 1
    assert kthSmallest(root, 2) == 2
    assert kthSmallest(root, 3) == 3
    assert kthSmallest(root, 4) == 4
    assert kthSmallest(root, 5) == 5
    assert kthSmallest(root, 6) == 6

    # Test 3: Single node
    root = build_tree([42])
    assert kthSmallest(root, 1) == 42

    # Test 4: Left-skewed tree
    root = build_tree([4,3,None,2,None,1])
    assert kthSmallest(root, 1) == 1
    assert kthSmallest(root, 4) == 4

    # Test 5: Right-skewed tree
    root = build_tree([1,None,2,None,3,None,4])
    assert kthSmallest(root, 3) == 3

    print("All tests passed.")

if __name__ == "__main__":
    test_kthSmallest()


