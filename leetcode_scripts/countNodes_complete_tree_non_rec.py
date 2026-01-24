class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root):
    """
    Counts the number of nodes in a complete binary tree.
    Uses binary search and bit manipulation for O((log n)^2) time.
    """
    if not root:
        return 0

    def get_depth(node):
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(idx, d, node):
        left, right = 0, 2**d - 1
        for _ in range(d):
            mid = (left + right) // 2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
            if not node:
                return False
        return True

    depth = get_depth(root)
    if depth == 0:
        return 1

    # Binary search to find how many nodes exist in the last level
    left, right = 0, 2**depth - 1
    while left <= right:
        mid = (left + right) // 2
        if exists(mid, depth, root):
            left = mid + 1
        else:
            right = mid - 1

    # Nodes above last level: 2^depth - 1, plus nodes in last level: left
    return (2**depth - 1) + left

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

    # Test 5: Only left children
    root = build_tree([1,2,None,3])
    assert countNodes(root) == 3

    # Test 6: Only right children (not complete, but valid input)
    root = build_tree([1,None,2,None,3])
    assert countNodes(root) == 3

    print("All tests passed.")

if __name__ == "__main__":
    test_countNodes()
