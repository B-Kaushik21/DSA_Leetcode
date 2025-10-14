class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # TIME COMPLEXITY : O(N*K)
        # SPACE COMPLEXITY : O(1)
        n=len(nums)
        for i in range(n-2*k+1):
            sub1=True
            sub2=True

            #first subarray[i,i+k)
            for j in range(i,i+k-1):
                if nums[j]>=nums[j+1]:
                    sub1=False
            #second subarry[i+k,i+2k)
            for j in range(i+k,i+2*k-1):
                if nums[j]>=nums[j+1]:
                    sub2=False
            if sub1 and sub2:
                return True
        return False

