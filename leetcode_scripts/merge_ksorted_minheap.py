class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

def mergeKLists(lists):
    """
    Merge k sorted linked lists and return it as one sorted list.
    Uses a min-heap for optimal performance.
    """
    heap = []
    # Counter to avoid comparison of ListNode when values are equal
    counter = 0
    for l in lists:
        if l:
            heapq.heappush(heap, (l.val, counter, l))
            counter += 1

    dummy = ListNode()
    curr = dummy

    while heap:
        val, _, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1

    return dummy.next

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

    # Test 5: All lists empty
    assert linked_to_list(mergeKLists([None, None, None])) == []

    # Test 6: Multiple lists with duplicates
    lists = [list_to_linked([1,4,5]), list_to_linked([1,3,4]), list_to_linked([2,6])]
    result = mergeKLists(lists)
    assert linked_to_list(result) == [1,1,2,3,4,4,5,6]

    # Test 7: Single node lists
    lists = [list_to_linked([i]) for i in [5,1,3,2,4]]
    result = mergeKLists(lists)
    assert linked_to_list(result) == [1,2,3,4,5]

    print("All tests passed for mergeKLists.")

if __name__ == "__main__":
    test_mergeKLists()
