class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root):
    """
    Given a binary tree containing digits from 0-9 only, each root-to-leaf path represents a number.
    Return the total sum of all the numbers formed by root-to-leaf paths.
    """
    def dfs(node, curr_sum):
        if not node:
            return 0
        curr_sum = curr_sum * 10 + node.val
        if not node.left and not node.right:
            return curr_sum
        return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
    return dfs(root, 0)

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
def test_sumNumbers():
    # Test 1: Example tree
    #     1
    #    / \
    #   2   3
    # Numbers: 12, 13
    root = build_tree([1,2,3])
    assert sumNumbers(root) == 25

    # Test 2: More complex tree
    #     4
    #    / \
    #   9   0
    #  / \
    # 5   1
    # Numbers: 495, 491, 40
    root = build_tree([4,9,0,5,1])
    assert sumNumbers(root) == 1026

    # Test 3: Single node
    root = build_tree([5])
    assert sumNumbers(root) == 5

    # Test 4: Empty tree
    root = build_tree([])
    assert sumNumbers(root) == 0

    # Test 5: Tree with zeros
    #     1
    #    / \
    #   0   1
    #  /
    # 5
    # Numbers: 105, 11
    root = build_tree([1,0,1,5])
    assert sumNumbers(root) == 116

    print("All test cases passed!")

test_sumNumbers()
