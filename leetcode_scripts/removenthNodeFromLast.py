class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    """
    Removes the nth node from the end of the list and returns its head.
    Args:
        head (ListNode): The head of the linked list.
        n (int): The position from the end to remove.
    Returns:
        ListNode: The head of the modified list.
    """
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove the nth node
    slow.next = slow.next.next

    return dummy.next

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
def test_removeNthFromEnd():
    # Test 1: Remove 2nd from end
    l1 = list_to_linkedlist([1,2,3,4,5])
    res1 = removeNthFromEnd(l1, 2)
    assert linkedlist_to_list(res1) == [1,2,3,5]

    # Test 2: Remove head
    l2 = list_to_linkedlist([1])
    res2 = removeNthFromEnd(l2, 1)
    assert linkedlist_to_list(res2) == []

    # Test 3: Remove last node
    l3 = list_to_linkedlist([1,2])
    res3 = removeNthFromEnd(l3, 1)
    assert linkedlist_to_list(res3) == [1]

    # Test 4: Remove first node in longer list
    l4 = list_to_linkedlist([1,2,3])
    res4 = removeNthFromEnd(l4, 3)
    assert linkedlist_to_list(res4) == [2,3]

    # Test 5: Remove middle node
    l5 = list_to_linkedlist([1,2,3,4])
    res5 = removeNthFromEnd(l5, 2)
    assert linkedlist_to_list(res5) == [1,2,4]

    print("All tests passed!")

test_removeNthFromEnd()
