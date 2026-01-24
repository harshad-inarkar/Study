class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    """
    Determines if a binary tree is symmetric around its center.
    Args:
        root (TreeNode): The root of the binary tree.
    Returns:
        bool: True if the tree is symmetric, False otherwise.
    """
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and \
               isMirror(t1.left, t2.right) and \
               isMirror(t1.right, t2.left)
    return isMirror(root, root)

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
def test_isSymmetric():
    # Test 1: Empty tree
    assert isSymmetric(None) == True

    # Test 2: Single node
    t2 = TreeNode(1)
    assert isSymmetric(t2) == True

    # Test 3: Symmetric tree
    t3 = list_to_tree([1,2,2,3,4,4,3])
    assert isSymmetric(t3) == True

    # Test 4: Asymmetric tree
    t4 = list_to_tree([1,2,2,None,3,None,3])
    assert isSymmetric(t4) == False

    # Test 5: Another asymmetric tree
    t5 = list_to_tree([1,2,2,None,3,None,3])
    assert isSymmetric(t5) == False

    # Test 6: Larger symmetric tree
    t6 = list_to_tree([1,2,2,3,4,4,3,5,None,None,5,5,None,None,5])
    assert isSymmetric(t6) == True

    print("All tests passed!")

test_isSymmetric()
# The bug is in the isSymmetric function: the recursive isMirror call is using t1.left, t2.right and t1.right, t2.left,
# but the order of recursion is wrong for the asymmetric case. The correct order is:
# isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
# However, the code above is correct in this respect, so the issue may be that the isSymmetric function is missing.
# Let's define isSymmetric and isMirror properly here.

def isSymmetric(root):
    """
    Determines if a binary tree is symmetric around its center.
    Args:
        root (TreeNode): The root of the binary tree.
    Returns:
        bool: True if the tree is symmetric, False otherwise.
    """
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and \
               isMirror(t1.left, t2.right) and \
               isMirror(t1.right, t2.left)
    return isMirror(root, root)

