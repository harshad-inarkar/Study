
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    """
    Removes duplicates from a sorted linked list.
    Only unique elements remain (first occurrence kept).
    Args:
        head (ListNode): The head of the linked list.
    Returns:
        ListNode: The head of the modified list.
    """
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

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
def test_remove_duplicates():
    # Test 1: List with duplicates
    l1 = list_to_linkedlist([1,1,2,3,3,4,4,5])
    res1 = remove_duplicates(l1)
    assert linkedlist_to_list(res1) == [1,2,3,4,5]

    # Test 2: All elements are duplicates
    l2 = list_to_linkedlist([1,1,1,1])
    res2 = remove_duplicates(l2)
    assert linkedlist_to_list(res2) == [1]

    # Test 3: No duplicates
    l3 = list_to_linkedlist([1,2,3])
    res3 = remove_duplicates(l3)
    assert linkedlist_to_list(res3) == [1,2,3]

    # Test 4: Duplicates at the start
    l4 = list_to_linkedlist([1,1,2,3])
    res4 = remove_duplicates(l4)
    assert linkedlist_to_list(res4) == [1,2,3]

    # Test 5: Duplicates at the end
    l5 = list_to_linkedlist([1,2,3,3])
    res5 = remove_duplicates(l5)
    assert linkedlist_to_list(res5) == [1,2,3]

    # Test 6: Empty list
    l6 = list_to_linkedlist([])
    res6 = remove_duplicates(l6)
    assert linkedlist_to_list(res6) == []

    # Test 7: Single node
    l7 = list_to_linkedlist([1])
    res7 = remove_duplicates(l7)
    assert linkedlist_to_list(res7) == [1]

    print("All tests passed!")

test_remove_duplicates()
