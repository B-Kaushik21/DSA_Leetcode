# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums=[]
        temp=head
        while temp.next:
            val=temp.val
            nums.append(val)
            temp=temp.next
        nums.append(temp.val)
        #print(nums)
        maxi=float('-inf')
        n=len(nums)
        for i in range(n):
            maxi=max(maxi,nums[i]+nums[n-1-i])
        return maxi