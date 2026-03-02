# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        for _ in range(k):
            if not temp:
                return head
            temp=temp.next
            
        p=None
        c=head
        for i in range(k):
            n=c.next
            c.next=p
            p=c
            c=n
        
        head.next=self.reverseKGroup(c,k)
        return p