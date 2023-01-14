class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        return previous