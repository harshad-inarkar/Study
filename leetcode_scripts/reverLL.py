class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    Reverses a singly linked list.
    Args:
        head (ListNode): The head of the linked list.
    Returns:
        ListNode: The new head of the reversed list.
    """
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

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
def test_reverseList():
    # Test 1: Normal list
    l1 = list_to_linkedlist([1,2,3,4,5])
    reversed_l1 = reverseList(l1)
    assert linkedlist_to_list(reversed_l1) == [5,4,3,2,1]

    # Test 2: Single element
    l2 = list_to_linkedlist([42])
    reversed_l2 = reverseList(l2)
    assert linkedlist_to_list(reversed_l2) == [42]

    # Test 3: Empty list
    l3 = list_to_linkedlist([])
    reversed_l3 = reverseList(l3)
    assert linkedlist_to_list(reversed_l3) == []

    # Test 4: Two elements
    l4 = list_to_linkedlist([1,2])
    reversed_l4 = reverseList(l4)
    assert linkedlist_to_list(reversed_l4) == [2,1]

    print("All tests passed!")

test_reverseList()
