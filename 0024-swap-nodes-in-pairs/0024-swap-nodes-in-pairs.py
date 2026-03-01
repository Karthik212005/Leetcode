# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode(0,head)
        p,cur=d,head
        while cur and cur.next:
            sec=cur.next
            npn=cur.next.next
            sec.next=cur
            cur.next=npn
            p.next=sec
            p=cur
            cur=npn
        return d.next


        

        