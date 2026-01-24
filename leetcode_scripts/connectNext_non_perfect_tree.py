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
    This works for any binary tree (not just perfect).
    """
    if not root:
        return None
    curr = root
    while curr:
        dummy = Node(0)
        tail = dummy
        while curr:
            if curr.left:
                tail.next = curr.left
                tail = tail.next
            if curr.right:
                tail.next = curr.right
                tail = tail.next
            curr = curr.next
        curr = dummy.next
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
        next_leftmost = None
        while curr:
            level.append(curr.val)
            if not next_leftmost:
                if curr.left:
                    next_leftmost = curr.left
                elif curr.right:
                    next_leftmost = curr.right
            curr = curr.next
        result.append(level)
        leftmost = next_leftmost
    return result

def build_tree_from_level_list(lst):
    """
    Builds a binary tree from a list (level order, None for missing nodes).
    Returns the root node.
    """
    if not lst:
        return None
    nodes = [Node(val) if val is not None else None for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def test_connect():
    # Test 1: Empty tree
    assert connect(None) == None

    # Test 2: Single node
    root = Node(1)
    connect(root)
    assert root.next is None

    # Test 3: Complete binary tree
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4  5  6   7
    root = build_tree_from_level_list([1,2,3,4,5,6,7])
    connect(root)
    assert level_order_next(root) == [[1],[2,3],[4,5,6,7]]

    # Test 4: Incomplete binary tree
    #        1
    #      /   \
    #     2     3
    #    /       \
    #   4         5
    root = build_tree_from_level_list([1,2,3,4,None,None,5])
    connect(root)
    assert level_order_next(root) == [[1],[2,3],[4,5]]

    # Test 5: Left-skewed tree
    #    1
    #   /
    #  2
    # /
    #3
    root = build_tree_from_level_list([1,2,None,3])
    connect(root)
    assert level_order_next(root) == [[1],[2],[3]]

    # Test 6: Right-skewed tree
    # 1
    #  \
    #   2
    #    \
    #     3
    root = build_tree_from_level_list([1,None,2,None,3])
    connect(root)
    assert level_order_next(root) == [[1],[2],[3]]

    # Test 7: Tree with random missing nodes
    #        1
    #      /   \
    #     2     3
    #      \      \
    #       5      4
    root = build_tree_from_level_list([1,2,3,None,5,None,4])
    connect(root)
    assert level_order_next(root) == [[1],[2,3],[5,4]]

    print("All tests passed!")

test_connect()
