class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    """
    Merges two sorted linked lists and returns the head of the new sorted list.
    """
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach the remaining nodes
    current.next = l1 if l1 else l2

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
def test_mergeTwoLists():
    # Test 1: Both lists non-empty
    l1 = list_to_linkedlist([1,2,4])
    l2 = list_to_linkedlist([1,3,4])
    merged = mergeTwoLists(l1, l2)
    assert linkedlist_to_list(merged) == [1,1,2,3,4,4]

    # Test 2: One list empty
    l1 = list_to_linkedlist([])
    l2 = list_to_linkedlist([0])
    merged = mergeTwoLists(l1, l2)
    assert linkedlist_to_list(merged) == [0]

    # Test 3: Both lists empty
    l1 = list_to_linkedlist([])
    l2 = list_to_linkedlist([])
    merged = mergeTwoLists(l1, l2)
    assert linkedlist_to_list(merged) == []

    # Test 4: Lists with different lengths
    l1 = list_to_linkedlist([2,5,7])
    l2 = list_to_linkedlist([1,3,4,6,8])
    merged = mergeTwoLists(l1, l2)
    assert linkedlist_to_list(merged) == [1,2,3,4,5,6,7,8]

    # Test 5: Lists with duplicate values
    l1 = list_to_linkedlist([1,3,5])
    l2 = list_to_linkedlist([1,1,2,3,4])
    merged = mergeTwoLists(l1, l2)
    assert linkedlist_to_list(merged) == [1,1,1,2,3,3,4,5]

    print("All tests passed!")

test_mergeTwoLists()
