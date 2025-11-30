class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totalsum=sum(nums)
        rem=totalsum%p
        if rem==0:
            return 0
        prefixmod={0:-1}
        prefixsum=0
        minlength=len(nums)
            
        for i,num in enumerate(nums):
            prefixsum+=num
            currentmod=prefixsum%p
            targetmod=(currentmod-rem+p)%p

            if targetmod in prefixmod:
                minlength=min(minlength,i-prefixmod[targetmod])
            prefixmod[currentmod]=i
        return minlength if minlength<len(nums) else -1