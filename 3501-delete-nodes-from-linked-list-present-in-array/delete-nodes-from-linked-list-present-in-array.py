# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        set_nums=set(nums)
        new=ListNode(0)
        tail=new

        temp=head
        while temp:
            val=temp.val
            temp=temp.next
            if val not in set_nums:
                tail.next=ListNode(val)
                tail=tail.next
        return new.next
        