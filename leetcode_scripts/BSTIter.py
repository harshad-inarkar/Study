class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        val = node.val
        if node.right:
            self._push_left(node.right)
        return val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

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
def test_BSTIterator():
    # Test 1: Basic BST
    #      7
    #     / \
    #    3   15
    #        / \
    #       9  20
    root = build_tree([7,3,15,None,None,9,20])
    it = BSTIterator(root)
    result = []
    while it.hasNext():
        result.append(it.next())
    assert result == [3,7,9,15,20]

    # Test 2: Single node
    root = build_tree([1])
    it = BSTIterator(root)
    assert it.hasNext() == True
    assert it.next() == 1
    assert it.hasNext() == False

    # Test 3: Empty tree
    root = build_tree([])
    it = BSTIterator(root)
    assert it.hasNext() == False

    # Test 4: Left-skewed tree
    #    3
    #   /
    #  2
    # /
    #1
    root = build_tree([3,2,None,1])
    it = BSTIterator(root)
    assert [it.next(), it.next(), it.next()] == [1,2,3]
    assert it.hasNext() == False

    # Test 5: Right-skewed tree
    # 1
    #  \
    #   2
    #    \
    #     3
    root = build_tree([1,None,2,None,3])
    it = BSTIterator(root)
    assert [it.next(), it.next(), it.next()] == [1,2,3]
    assert it.hasNext() == False
