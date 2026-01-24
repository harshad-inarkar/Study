class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    Adds two numbers represented by linked lists.
    Each node contains a single digit and the digits are stored in reverse order.
    Returns the sum as a linked list in the same reverse order.
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next

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
def test_addTwoNumbers():
    # 342 + 465 = 807
    l1 = list_to_linkedlist([2,4,3])
    l2 = list_to_linkedlist([5,6,4])
    result = addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [7,0,8]

    # 0 + 0 = 0
    l1 = list_to_linkedlist([0])
    l2 = list_to_linkedlist([0])
    result = addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0]

    # 9999 + 1 = 10000
    l1 = list_to_linkedlist([9,9,9,9])
    l2 = list_to_linkedlist([1])
    result = addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0,0,0,0,1]

    # 123 + 987 = 1110
    l1 = list_to_linkedlist([3,2,1])
    l2 = list_to_linkedlist([7,8,9])
    result = addTwoNumbers(l1, l2)
    assert linkedlist_to_list(result) == [0,1,1,1]

    print("All tests passed!")

test_addTwoNumbers()
