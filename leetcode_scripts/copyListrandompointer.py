class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: 'Node') -> 'Node':
    """
    Creates a deep copy of a linked list where each node has a random pointer.
    """
    if not head:
        return None

    # Step 1: Insert new nodes after each original node
    curr = head
    while curr:
        new_node = Node(curr.val, curr.next)
        curr.next = new_node
        curr = new_node.next

    # Step 2: Assign random pointers for the new nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate the new list from the original list
    curr = head
    pseudo_head = Node(0)
    copy_curr = pseudo_head
    while curr:
        copy = curr.next
        curr.next = copy.next
        copy_curr.next = copy
        copy_curr = copy
        curr = curr.next

    return pseudo_head.next

# Helper functions for testing
def build_linked_list_with_random(arr, random_indices):
    """
    arr: list of values
    random_indices: list of indices for random pointers, or None
    Returns the head of the linked list.
    """
    if not arr:
        return None
    nodes = [Node(val) for val in arr]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    for i, rand_idx in enumerate(random_indices):
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]

def linked_list_to_lists(head):
    """
    Returns two lists:
    - values: list of node values
    - random_indices: for each node, the index of its random pointer or None
    """
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next
    values = [n.val for n in nodes]
    node_to_index = {n: i for i, n in enumerate(nodes)}
    random_indices = []
    for n in nodes:
        if n.random is not None:
            random_indices.append(node_to_index[n.random])
        else:
            random_indices.append(None)
    return values, random_indices

# Tests
def test_copyRandomList():
    # Test 1: Example with random pointers
    arr = [7, 13, 11, 10, 1]
    random_indices = [None, 0, 4, 2, 0]
    head = build_linked_list_with_random(arr, random_indices)
    copied = copyRandomList(head)
    vals, rands = linked_list_to_lists(copied)
    assert vals == arr
    assert rands == random_indices

    # Test 2: Empty list
    head = build_linked_list_with_random([], [])
    copied = copyRandomList(head)
    assert copied is None

    # Test 3: Single node, random points to itself
    arr = [42]
    random_indices = [0]
    head = build_linked_list_with_random(arr, random_indices)
    copied = copyRandomList(head)
    vals, rands = linked_list_to_lists(copied)
    assert vals == arr
    assert rands == random_indices

    # Test 4: Two nodes, no randoms
    arr = [1, 2]
    random_indices = [None, None]
    head = build_linked_list_with_random(arr, random_indices)
    copied = copyRandomList(head)
    vals, rands = linked_list_to_lists(copied)
    assert vals == arr
    assert rands == random_indices

    # Test 5: Two nodes, cross randoms
    arr = [1, 2]
    random_indices = [1, 0]
    head = build_linked_list_with_random(arr, random_indices)
    copied = copyRandomList(head)
    vals, rands = linked_list_to_lists(copied)
    assert vals == arr
    assert rands == random_indices

    print("All tests passed!")

test_copyRandomList()

