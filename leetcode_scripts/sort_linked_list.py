class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sort_linked_list(head):
    # Merge sort for linked list
    if not head or not head.next:
        return head

    # Find the middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sort_linked_list(head)
    right = sort_linked_list(mid)

    return merge(left, right)

def merge(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
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
def test_sort_linked_list():
    cases = [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([5, 3, 8, 2, 1], [1, 2, 3, 5, 8]),
        ([3, 3, 3], [3, 3, 3]),
        ([10, -1, 2, 0], [-1, 0, 2, 10])
    ]
    for i, (input_list, expected) in enumerate(cases):
        head = list_to_linked(input_list)
        sorted_head = sort_linked_list(head)
        output = linked_to_list(sorted_head)
        assert output == expected, f"Test case {i+1} failed: got {output}, expected {expected}"
    print("All test cases passed.")

if __name__ == "__main__":
    test_sort_linked_list()
