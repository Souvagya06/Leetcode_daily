class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Find length and last node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        # Make circular list
        tail.next = head

        # Find new tail
        steps = length - k - 1
        newTail = head
        for _ in range(steps):
            newTail = newTail.next

        # New head
        newHead = newTail.next

        # Break the circle
        newTail.next = None

        return newHead