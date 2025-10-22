class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        store=self.helper(nums,k,numOperations)
        left=0
        otherMaxFreq=0
        for right in range(len(nums)):
            while nums[right]>nums[left]+2*k:
                left+=1
            otherMaxFreq=max(otherMaxFreq,right-left+1)
            if otherMaxFreq>=numOperations:
                otherMaxFreq=numOperations
                break
        return max(store,otherMaxFreq)
    def helper(self,nums,k,numOperations):
        count=Counter(nums)
        maxFreq=0
        for val in count.keys():
            left=bisect_left(nums,val-k)
            right=bisect_right(nums,val+k)-1
            freq=min(right-left+1,numOperations+count[val])
            maxFreq=max(maxFreq,freq)
        return maxFreq