from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root):
    """
    Returns a list of the average value of nodes on each level.
    """
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_sum = 0
        level_count = len(queue)
        for _ in range(level_count):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_sum / level_count)
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
def test_averageOfLevels():
    # Test 1: Example tree
    #      3
    #     / \
    #    9  20
    #       / \
    #      15  7
    root = build_tree([3,9,20,None,None,15,7])
    assert averageOfLevels(root) == [3.0, 14.5, 11.0]

    # Test 2: Single node
    root = build_tree([5])
    assert averageOfLevels(root) == [5.0]

    # Test 3: Empty tree
    root = build_tree([])
    assert averageOfLevels(root) == []

    # Test 4: Tree with negative values
    root = build_tree([1,-2,3,-4,-5,6,7])
    assert averageOfLevels(root) == [1.0, 0.5, 1.0]

    print("All tests passed.")

if __name__ == "__main__":
    test_averageOfLevels()
