class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            f=head
            s=head
        
            for _ in range(n):
                f=f.next
            if not f:
                return head.next
            
            while f.next:
                f=f.next
                s=s.next

            
            s.next=s.next.next
            
            
            return head