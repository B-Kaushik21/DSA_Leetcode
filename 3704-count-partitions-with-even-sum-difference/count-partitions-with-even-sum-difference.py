class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count,n=0,len(nums)
        prefix=[0]*n
        prefix[0]=nums[0]

        for i in range(1,n):
            prefix[i]=nums[i]+prefix[i-1]
        total=prefix[-1]
        for i in range(n-1):
            left=prefix[i]
            right=total-left
            if (left-right)%2==0:
                count+=1
        return count
            