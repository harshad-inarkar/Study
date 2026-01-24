class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    """
    Populates each next pointer to point to its next right node.
    If there is no next right node, the next pointer should be set to None.
    This works for perfect binary trees.
    """
    if not root:
        return None
    leftmost = root
    while leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
            head = head.next
        leftmost = leftmost.left
    return root

def level_order_next(root):
    """
    Returns a list of lists, where each inner list contains the node values
    at that level, traversed using the next pointers.
    """
    result = []
    leftmost = root
    while leftmost:
        curr = leftmost
        level = []
        while curr:
            level.append(curr.val)
            curr = curr.next
        result.append(level)
        leftmost = leftmost.left
    return result

def build_perfect_binary_tree(values):
    """
    Builds a perfect binary tree from a list of values (level order).
    Returns the root node.
    """
    if not values:
        return None
    nodes = [Node(val) for val in values]
    n = len(nodes)
    for i in range(n):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < n:
            nodes[i].left = nodes[left_idx]
        if right_idx < n:
            nodes[i].right = nodes[right_idx]
    return nodes[0]

def test_connect():
    # Test 1: Example tree
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4  5  6   7
    vals = [1,2,3,4,5,6,7]
    root = build_perfect_binary_tree(vals)
    connect(root)
    assert level_order_next(root) == [[1], [2,3], [4,5,6,7]]

    # Test 2: Single node
    root = Node(10)
    connect(root)
    assert level_order_next(root) == [[10]]

    # Test 3: Empty tree
    assert connect(None) == None

    # Test 4: Larger perfect tree
    vals = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    root = build_perfect_binary_tree(vals)
    connect(root)
    assert level_order_next(root) == [
        [1],
        [2,3],
        [4,5,6,7],
        [8,9,10,11,12,13,14,15]
    ]

    print("All tests passed!")

if __name__ == "__main__":
    test_connect()

