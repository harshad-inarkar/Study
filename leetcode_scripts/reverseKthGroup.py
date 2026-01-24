class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    """
    Reverses nodes of a linked list in k-group chunks.
    If the number of nodes is not a multiple of k, the last nodes remain as is.
    Args:
        head (ListNode): The head of the linked list.
        k (int): The group size to reverse.
    Returns:
        ListNode: The head of the modified list.
    """
    def get_kth(curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy

    while True:
        kth = get_kth(group_prev, k)
        if not kth:
            break
        group_next = kth.next

        # Reverse group
        prev, curr = kth.next, group_prev.next
        while curr != group_next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp

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
def test_reverseKGroup():
    # Test 1: k divides length
    l1 = list_to_linkedlist([1,2,3,4,5,6])
    res1 = reverseKGroup(l1, 2)
    assert linkedlist_to_list(res1) == [2,1,4,3,6,5]

    # Test 2: k does not divide length
    l2 = list_to_linkedlist([1,2,3,4,5])
    res2 = reverseKGroup(l2, 3)
    assert linkedlist_to_list(res2) == [3,2,1,4,5]

    # Test 3: k = 1 (no change)
    l3 = list_to_linkedlist([1,2,3])
    res3 = reverseKGroup(l3, 1)
    assert linkedlist_to_list(res3) == [1,2,3]

    # Test 4: k > length (no change)
    l4 = list_to_linkedlist([1,2])
    res4 = reverseKGroup(l4, 3)
    assert linkedlist_to_list(res4) == [1,2]

    # Test 5: Empty list
    l5 = list_to_linkedlist([])
    res5 = reverseKGroup(l5, 2)
    assert linkedlist_to_list(res5) == []

    # Test 6: Single element, k=1
    l6 = list_to_linkedlist([42])
    res6 = reverseKGroup(l6, 1)
    assert linkedlist_to_list(res6) == [42]

    print("All tests passed!")

test_reverseKGroup()
