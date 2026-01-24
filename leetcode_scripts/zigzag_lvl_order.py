from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    """
    Returns the zigzag level order traversal of a binary tree.
    """
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level_size = len(queue)
        level = deque()
        while level_size:
            node = queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
            level_size -= 1
        result.append(list(level))
        left_to_right = not left_to_right
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
def test_zigzagLevelOrder():
    # Test 1: Example tree
    #      3
    #     / \
    #    9  20
    #       / \
    #      15  7
    root = build_tree([3,9,20,None,None,15,7])
    assert zigzagLevelOrder(root) == [[3],[20,9],[15,7]]

    # Test 2: Single node
    root = build_tree([1])
    assert zigzagLevelOrder(root) == [[1]]

    # Test 3: Empty tree
    root = build_tree([])
    assert zigzagLevelOrder(root) == []

    # Test 4: Left-skewed tree
    root = build_tree([1,2,None,3,None,4])
    assert zigzagLevelOrder(root) == [[1],[2],[3],[4]]

    # Test 5: Right-skewed tree
    root = build_tree([1,None,2,None,3,None,4])
    assert zigzagLevelOrder(root) == [[1],[2],[3],[4]]

    # Test 6: More complex tree
    root = build_tree([1,2,3,4,None,None,5])
    assert zigzagLevelOrder(root) == [[1],[3,2],[4,5]]

    print("All tests passed.")

if __name__ == "__main__":
    test_zigzagLevelOrder()
