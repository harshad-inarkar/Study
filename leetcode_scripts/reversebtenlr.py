class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    """
    Reverses the nodes of a linked list from position left to right (1-indexed).
    Args:
        head (ListNode): The head of the linked list.
        left (int): The starting position.
        right (int): The ending position.
    Returns:
        ListNode: The head of the modified list.
    """
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move prev to the node before the reversal starts
    for _ in range(left - 1):
        prev = prev.next

    # Reverse the sublist
    curr = prev.next
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next

# Helper functions for testing
def list_to_linkedlist(lst):
    if not lst:
        return None
    
    head = ListNode(lst[0])
    curr = head
    for i in range(1, len(lst)):
        curr.next = ListNode(lst[i])
        curr = curr.next
    return head

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Tests
def test_reverseBetween():
    # Test 1: Reverse middle part
    l1 = list_to_linkedlist([1,2,3,4,5])
    res1 = reverseBetween(l1, 2, 4)
    assert linkedlist_to_list(res1) == [1,4,3,2,5]

    # Test 2: Reverse entire list
    l2 = list_to_linkedlist([1,2,3,4,5])
    res2 = reverseBetween(l2, 1, 5)
    assert linkedlist_to_list(res2) == [5,4,3,2,1]

    # Test 3: Reverse single element (no change)
    l3 = list_to_linkedlist([1,2,3])
    res3 = reverseBetween(l3, 2, 2)
    assert linkedlist_to_list(res3) == [1,2,3]

    # Test 4: Reverse at head
    l4 = list_to_linkedlist([1,2,3,4])
    res4 = reverseBetween(l4, 1, 2)
    assert linkedlist_to_list(res4) == [2,1,3,4]

    # Test 5: Reverse at tail
    l5 = list_to_linkedlist([1,2,3,4])
    res5 = reverseBetween(l5, 3, 4)
    assert linkedlist_to_list(res5) == [1,2,4,3]

    # Test 6: Single node list
    l6 = list_to_linkedlist([1])
    res6 = reverseBetween(l6, 1, 1)
    assert linkedlist_to_list(res6) == [1]

    print("All tests passed!")

test_reverseBetween()
