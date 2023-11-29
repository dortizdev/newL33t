class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        return prev