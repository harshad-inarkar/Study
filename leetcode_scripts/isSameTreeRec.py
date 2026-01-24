class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    """
    Determines if two binary trees are the same.
    Args:
        p (TreeNode): Root of the first tree.
        q (TreeNode): Root of the second tree.
    Returns:
        bool: True if both trees are identical, False otherwise.
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

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
def test_isSameTree():
    # Test 1: Both trees empty
    assert isSameTree(None, None) == True

    # Test 2: One tree empty, one not
    t1 = list_to_tree([1,2,3])
    assert isSameTree(t1, None) == False
    assert isSameTree(None, t1) == False

    # Test 3: Identical trees
    t2 = list_to_tree([1,2,3])
    t3 = list_to_tree([1,2,3])
    assert isSameTree(t2, t3) == True

    # Test 4: Different structure
    t4 = list_to_tree([1,2])
    t5 = list_to_tree([1,None,2])
    assert isSameTree(t4, t5) == False

    # Test 5: Different values
    t6 = list_to_tree([1,2,1])
    t7 = list_to_tree([1,1,2])
    assert isSameTree(t6, t7) == False

    # Test 6: Both single node, same value
    t8 = TreeNode(5)
    t9 = TreeNode(5)
    assert isSameTree(t8, t9) == True

    # Test 7: Both single node, different value
    t10 = TreeNode(5)
    t11 = TreeNode(6)
    assert isSameTree(t10, t11) == False

    print("All tests passed!")

test_isSameTree()
