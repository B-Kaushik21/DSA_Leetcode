class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        N=len(nums)
        n=N//2
        store={}
        for i in range(N):
            if nums[i] in store:
                store[nums[i]]+=1
            else:
                store[nums[i]]=1
        for key,val in store.items():
            if val==n:
                return key
        
