# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the head of the result list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Loop while there are nodes to process in l1 or l2, or there is a remaining carry
        while l1 or l2 or carry:
            # Get values if nodes exist, otherwise use 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum and update the carry
            total = val1 + val2 + carry
            carry = total // 10
            out_val = total % 10
            
            # Create a new node with the digit and attach it to the result list
            current.next = ListNode(out_val)
            current = current.next
            
            # Move to the next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy.next