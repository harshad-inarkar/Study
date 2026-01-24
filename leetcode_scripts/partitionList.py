class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    """
    Partitions a linked list around a value x, such that all nodes less than x come before nodes greater than or equal to x.
    The original relative order of the nodes in each of the two partitions should be preserved.
    Args:
        head (ListNode): The head of the linked list.
        x (int): The partition value.
    Returns:
        ListNode: The head of the partitioned list.
    """
    before_head = ListNode(0)
    before = before_head
    after_head = ListNode(0)
    after = after_head

    curr = head
    while curr:
        if curr.val < x:
            before.next = curr
            before = before.next
        else:
            after.next = curr
            after = after.next
        curr = curr.next

    after.next = None
    before.next = after_head.next
    return before_head.next

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
def test_partition():
    # Test 1: Mixed values
    l1 = list_to_linkedlist([1,4,3,2,5,2])
    res1 = partition(l1, 3)
    assert linkedlist_to_list(res1) == [1,2,2,4,3,5]

    # Test 2: All less than x
    l2 = list_to_linkedlist([1,1,2])
    res2 = partition(l2, 3)
    assert linkedlist_to_list(res2) == [1,1,2]

    # Test 3: All greater than or equal to x
    l3 = list_to_linkedlist([4,5,6])
    res3 = partition(l3, 3)
    assert linkedlist_to_list(res3) == [4,5,6]

    # Test 4: Empty list
    l4 = list_to_linkedlist([])
    res4 = partition(l4, 1)
    assert linkedlist_to_list(res4) == []

    # Test 5: x is less than all elements
    l5 = list_to_linkedlist([3,4,5])
    res5 = partition(l5, 1)
    assert linkedlist_to_list(res5) == [3,4,5]

    # Test 6: x is greater than all elements
    l6 = list_to_linkedlist([1,2,2])
    res6 = partition(l6, 10)
    assert linkedlist_to_list(res6) == [1,2,2]

    # Test 7: Single node
    l7 = list_to_linkedlist([2])
    res7 = partition(l7, 2)
    assert linkedlist_to_list(res7) == [2]

    print("All tests passed!")

test_partition()
