
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    """
    Returns the values of the nodes you can see from the right side.
    Uses collections.deque for efficient queue operations.
    """
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
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
def test_rightSideView():
    # Test 1: Example tree
    #      1
    #     / \
    #    2   3
    #     \   \
    #      5   4
    root = build_tree([1,2,3,None,5,None,4])
    assert rightSideView(root) == [1,3,4]

    # Test 2: Single node
    root = build_tree([1])
    assert rightSideView(root) == [1]

    # Test 3: Empty tree
    root = build_tree([])
    assert rightSideView(root) == []

    # Test 4: Left-skewed tree
    #    1
    #   /
    #  2
    # /
    #3
    root = build_tree([1,2,None,3])
    assert rightSideView(root) == [1,2,3]

    # Test 5: Right-skewed tree
    # 1
    #  \
    #   2
    #    \
    #     3
    root = build_tree([1,None,2,None,3])
    assert rightSideView(root) == [1,2,3]

    print("All tests passed.")

if __name__ == "__main__":
    test_rightSideView()
