class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderRecursive(root):
    """
    Returns the level order traversal of a binary tree using recursion.
    """
    def helper(node, level, result):
        if not node:
            return
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        helper(node.left, level + 1, result)
        helper(node.right, level + 1, result)

    result = []
    helper(root, 0, result)
    return result

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
def test_levelOrderRecursive():
    # Test 1: Example tree
    #      3
    #     / \
    #    9  20
    #       / \
    #      15  7
    root = build_tree([3,9,20,None,None,15,7])
    assert levelOrderRecursive(root) == [[3],[9,20],[15,7]]

    # Test 2: Single node
    root = build_tree([1])
    assert levelOrderRecursive(root) == [[1]]

    # Test 3: Empty tree
    root = build_tree([])
    assert levelOrderRecursive(root) == []

    # Test 4: Left-skewed tree
    root = build_tree([1,2,None,3,None,4])
    assert levelOrderRecursive(root) == [[1],[2],[3],[4]]

    # Test 5: Right-skewed tree
    root = build_tree([1,None,2,None,3,None,4])
    assert levelOrderRecursive(root) == [[1],[2],[3],[4]]

    print("All tests passed.")

if __name__ == "__main__":
    test_levelOrderRecursive()
