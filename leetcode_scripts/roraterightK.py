class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    """
    Rotates the linked list to the right by k places.
    Args:
        head (ListNode): The head of the linked list.
        k (int): Number of places to rotate.
    Returns:
        ListNode: The head of the rotated list.
    """
    if not head or not head.next or k == 0:
        return head

    # Compute the length and get the tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    k = k % length
    if k == 0:
        return head

    # Find the new tail: (length - k - 1)th node
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    tail.next = head

    return new_head

# Helper functions for testing
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Tests
def test_rotateRight():
    # Test 1: Rotate by 2
    l1 = list_to_linkedlist([1,2,3,4,5])
    res1 = rotateRight(l1, 2)
    assert linkedlist_to_list(res1) == [4,5,1,2,3]

    # Test 2: Rotate by 0 (no change)
    l2 = list_to_linkedlist([0,1,2])
    res2 = rotateRight(l2, 0)
    assert linkedlist_to_list(res2) == [0,1,2]

    # Test 3: Rotate by length (no change)
    l3 = list_to_linkedlist([1,2,3])
    res3 = rotateRight(l3, 3)
    assert linkedlist_to_list(res3) == [1,2,3]

    # Test 4: Rotate by more than length
    l4 = list_to_linkedlist([1,2])
    res4 = rotateRight(l4, 5)
    assert linkedlist_to_list(res4) == [2,1]

    # Test 5: Single node
    l5 = list_to_linkedlist([1])
    res5 = rotateRight(l5, 99)
    assert linkedlist_to_list(res5) == [1]

    # Test 6: Empty list
    l6 = list_to_linkedlist([])
    res6 = rotateRight(l6, 3)
    assert linkedlist_to_list(res6) == []

    print("All tests passed!")

test_rotateRight()
