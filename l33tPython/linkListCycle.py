class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t, h = head, head
        #Tortoise and Hare solution

        while h and h.next:
            t = t.next
            h = h.next.next
            if h == t:
                return True

        return False