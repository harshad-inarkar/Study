class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    """
    Inverts a binary tree.
    Args:
        root (TreeNode): The root of the binary tree.
    Returns:
        TreeNode: The root of the inverted binary tree.
    """
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

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

# Helper function to convert tree to list (level order)
def tree_to_list(root):
    from collections import deque
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

# Tests
def test_invertTree():
    # Test 1: Empty tree
    assert invertTree(None) == None

    # Test 2: Single node
    t2 = TreeNode(1)
    inv2 = invertTree(t2)
    assert tree_to_list(inv2) == [1]

    # Test 3: Complete binary tree
    t3 = list_to_tree([4,2,7,1,3,6,9])
    inv3 = invertTree(t3)
    assert tree_to_list(inv3) == [4,7,2,9,6,3,1]

    # Test 4: Left-skewed tree
    t4 = list_to_tree([1,2,None,3])
    inv4 = invertTree(t4)
    assert tree_to_list(inv4) == [1,None,2,None,3]

    # Test 5: Right-skewed tree
    t5 = list_to_tree([1,None,2,None,3])
    inv5 = invertTree(t5)
    assert tree_to_list(inv5) == [1,2,None,3]

    print("All tests passed!")

test_invertTree()
