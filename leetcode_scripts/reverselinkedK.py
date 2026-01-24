def reverseKGroup(head, k):
    if not head or k == 1:
        return head
    
    # Helper function to get length of linked list
    def getLength(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length
    
    # Helper function to reverse a portion of linked list
    def reverseList(start, end):
        prev = None
        curr = start
        while prev != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy
    length = getLength(head)
    
    while length >= k:
        curr = prev_group.next
        next_group = curr
        
        # Move k-1 steps forward to find end of current group
        for i in range(k-1):
            curr = curr.next
            
        # Save next group's head
        temp = curr.next
        
        # Reverse current group
        reversed_head = reverseList(prev_group.next, curr)
        
        # Connect with previous group
        prev_group.next = reversed_head
        
        # Connect with next group
        next_group.next = temp
        
        # Update prev_group for next iteration
        prev_group = next_group
        length -= k
        
    return dummy.next
