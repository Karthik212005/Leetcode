# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        temp=head
        l=1
        while temp.next:
            temp=temp.next
            l+=1
        pos=k%l
        if pos==0:
            return head
        c=head
        for _ in range(l-pos-1):
            c=c.next
        h2=c.next
        c.next=None
        temp.next=head
        return h2