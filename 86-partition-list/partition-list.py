# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less,more=ListNode(0),ListNode(0)
        l,m=less,more
        temp=head
        while temp:
            nxt=temp.next #save next node
            if temp.val<x:
                l.next=temp
                l=l.next
            else:
                m.next=temp
                m=m.next
            temp.next=None #detach
            temp=nxt
        l.next=more.next
        return less.next 