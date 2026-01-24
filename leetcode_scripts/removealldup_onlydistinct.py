class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_all_duplicates(head):
    """
    Removes all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
    Args:
        head (ListNode): The head of the linked list.
    Returns:
        ListNode: The head of the modified list with all duplicates removed.
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        duplicate = False
        # Check if current node is a start of duplicates
        while curr.next and curr.val == curr.next.val:
            duplicate = True
            curr = curr.next
        if duplicate:
            # Skip all duplicates
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next

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
def test_remove_all_duplicates():
    # Test 1: List with duplicates
    l1 = list_to_linkedlist([1,2,3,3,4,4,5])
    res1 = remove_all_duplicates(l1)
    assert linkedlist_to_list(res1) == [1,2,5]

    # Test 2: All elements are duplicates
    l2 = list_to_linkedlist([1,1,1,1])
    res2 = remove_all_duplicates(l2)
    assert linkedlist_to_list(res2) == []

    # Test 3: No duplicates
    l3 = list_to_linkedlist([1,2,3])
    res3 = remove_all_duplicates(l3)
    assert linkedlist_to_list(res3) == [1,2,3]

    # Test 4: Duplicates at the start
    l4 = list_to_linkedlist([1,1,2,3])
    res4 = remove_all_duplicates(l4)
    assert linkedlist_to_list(res4) == [2,3]

    # Test 5: Duplicates at the end
    l5 = list_to_linkedlist([1,2,3,3])
    res5 = remove_all_duplicates(l5)
    assert linkedlist_to_list(res5) == [1,2]

    # Test 6: Empty list
    l6 = list_to_linkedlist([])
    res6 = remove_all_duplicates(l6)
    assert linkedlist_to_list(res6) == []

    # Test 7: Single node
    l7 = list_to_linkedlist([1])
    res7 = remove_all_duplicates(l7)
    assert linkedlist_to_list(res7) == [1]

    print("All tests passed!")

test_remove_all_duplicates()
