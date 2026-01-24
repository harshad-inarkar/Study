class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root):
    """
    Counts the number of nodes in a complete binary tree using recursion.
    """
    if not root:
        return 0

    # Compute left and right depth
    def get_depth(node):
        d = 0
        while node:
            node = node.left
            d += 1
        return d

 
    l = get_depth(root.left)
    r = get_depth(root.right)
    if l == r:
        # Perfect binary tree
        return (1 << l) + countNodes(root.right)
    else:
        return (1 << r) + countNodes(root.left) 

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
def test_countNodes():
    # Test 1: Complete tree
    #      1
    #     / \
    #    2   3
    #   / \  /
    #  4  5 6
    root = build_tree([1,2,3,4,5,6])
    assert countNodes(root) == 6

    # Test 2: Full tree
    #      1
    #     / \
    #    2   3
    #   / \ / \
    #  4  5 6  7
    root = build_tree([1,2,3,4,5,6,7])
    assert countNodes(root) == 7

    # Test 3: Single node
    root = build_tree([1])
    assert countNodes(root) == 1

    # Test 4: Empty tree
    root = build_tree([])
    assert countNodes(root) == 0

    # Non Complete tree
    # # Test 5: Only left children
    # root = build_tree([1,2,None,3])
    # assert countNodes(root) == 3

    # # Test 6: Only right children (not complete, but valid input)
    # root = build_tree([1,None,2,None,3])
    # assert countNodes(root) == 3

    print("All tests passed.")

if __name__ == "__main__":
    test_countNodes()
