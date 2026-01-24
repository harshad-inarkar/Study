class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    Merge k sorted linked lists using divide and conquer approach.
    """
    if not lists or len(lists) == 0:
        return None

    def mergeTwo(l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

    def mergeRange(lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        l1 = mergeRange(lists, left, mid)
        l2 = mergeRange(lists, mid+1, right)
        return mergeTwo(l1, l2)

    return mergeRange(lists, 0, len(lists)-1)

# Helper functions for testing
def list_to_linked(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# Tests
def test_mergeKLists():
    # Test 1: All lists empty
    assert linked_to_list(mergeKLists([])) == []
    assert linked_to_list(mergeKLists([None, None])) == []

    # Test 2: Single list
    l1 = list_to_linked([1,2,3])
    assert linked_to_list(mergeKLists([l1])) == [1,2,3]

    # Test 3: Two lists
    l1 = list_to_linked([1,4,5])
    l2 = list_to_linked([1,3,4])
    result = mergeKLists([l1, l2])
    assert linked_to_list(result) == [1,1,3,4,4,5]

    # Test 4: Three lists, one empty
    l1 = list_to_linked([2,6])
    l2 = None
    l3 = list_to_linked([0,7])
    result = mergeKLists([l1, l2, l3])
    assert linked_to_list(result) == [0,2,6,7]

    # Test 5: Many lists
    lists = [list_to_linked([i]) for i in [1,3,5,7,9]]
    result = mergeKLists(lists)
    assert linked_to_list(result) == [1,3,5,7,9]

    # Test 6: Lists with duplicates
    l1 = list_to_linked([1,4,4])
    l2 = list_to_linked([2,4,5])
    l3 = list_to_linked([2,6])
    result = mergeKLists([l1, l2, l3])
    assert linked_to_list(result) == [1,2,2,4,4,4,5,6]

    print("All tests passed!")

test_mergeKLists()
