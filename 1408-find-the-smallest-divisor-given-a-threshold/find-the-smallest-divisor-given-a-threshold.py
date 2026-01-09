class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        n=len(nums)
        res=high
        while low<=high:
            mid=(low+high)//2
            val=0
            for num in nums:
                val+=ceil(num/mid)
            if val<=threshold:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
            
    

