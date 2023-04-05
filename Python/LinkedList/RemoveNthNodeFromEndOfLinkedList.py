# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Create a dummy node to handle edge case where the head node is removed.
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers: slow and fast.
        slow = fast = dummy
        
        # Move the fast pointer n+1 times ahead of the slow pointer.
        for i in range(n + 1):
            fast = fast.next
        
        # Move both pointers one node at a time until the fast pointer reaches the end of the list.
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Remove the target node by setting slow.next to slow.next.next.
        slow.next = slow.next.next
        
        # Return the head of the modified linked list.
        return dummy.next
