class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]

        for num in nums:
            if num==2:
                res.append(-1)
                continue
            temp=num
            count=0
            #count consecutive 1's from the right
            while num&1==1:
                count+=1
                num//=2
            res.append(temp-2**(count-1))
        return res