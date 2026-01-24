class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    """
    Detects if a linked list has a cycle.
    Args:
        head (ListNode): The head of the linked list.
    Returns:
        bool: True if there is a cycle, False otherwise.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Tests
def test_hasCycle():
    # Helper to create a list with or without a cycle
    def create_list(values, pos):
        nodes = [ListNode(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]
        if pos != -1:
            nodes[-1].next = nodes[pos]
        return nodes[0] if nodes else None

    # No cycle
    head1 = create_list([3,2,0,-4], -1)
    assert hasCycle(head1) == False

    # Cycle at position 1
    head2 = create_list([3,2,0,-4], 1)
    assert hasCycle(head2) == True

    # Single node, no cycle
    head3 = create_list([1], -1)
    assert hasCycle(head3) == False

    # Single node, cycle to itself
    head4 = create_list([1], 0)
    assert hasCycle(head4) == True

    # Empty list
    head5 = create_list([], -1)
    assert hasCycle(head5) == False

    print("All tests passed!")

test_hasCycle()
