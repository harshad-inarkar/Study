class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    """
    Flattens the binary tree to a linked list in-place (preorder traversal).
    After flattening, the left of each node should point to None and the right should point to the next node in preorder.
    """
    curr = root
    while curr:
        if curr.left:
            # Find the rightmost node of left subtree
            prev = curr.left
            while prev.right:
                prev = prev.right
            # Connect right subtree to the rightmost node
            prev.right = curr.right
            # Move left subtree to right
            curr.right = curr.left
            curr.left = None
        curr = curr.right

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

# Helper function to get flattened tree as list
def flattened_to_list(root):
    res = []
    curr = root
    while curr:
        res.append(curr.val)
        if curr.left:
            raise Exception("Tree not properly flattened: left child exists")
        curr = curr.right
    return res

# Tests
def test_flatten():
    # Test 1: Example tree
    #     1
    #    / \
    #   2   5
    #  / \   \
    # 3   4   6
    root = build_tree([1,2,5,3,4,None,6])
    flatten(root)
    assert flattened_to_list(root) == [1,2,3,4,5,6]

    # Test 2: Empty tree
    root = build_tree([])
    flatten(root)
    assert root is None

    # Test 3: Single node
    root = build_tree([1])
    flatten(root)
    assert flattened_to_list(root) == [1]

    # Test 4: Left-skewed tree
    root = build_tree([1,2,None,3,None,4,None])
    flatten(root)
    assert flattened_to_list(root) == [1,2,3,4]

    # Test 5: Right-skewed tree
    root = build_tree([1,None,2,None,3,None,4])
    flatten(root)
    assert flattened_to_list(root) == [1,2,3,4]

    print("All test cases passed!")

test_flatten()
