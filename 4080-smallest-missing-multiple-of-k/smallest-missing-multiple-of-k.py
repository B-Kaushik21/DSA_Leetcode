class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        freq=set()
        for i in range(len(nums)):
            if nums[i]%k==0:
                freq.add(nums[i])
        if len(freq)==0:
            return k
        temp=max(freq)//k
        length=len(freq)
        print(length)
        for i in range(1,length+1):
            if k*i not in freq:
                return k*i
        return temp*k+k