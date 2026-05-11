class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            n=len(str(num))
            tmp=[]
            while n>0:
                tmp.append(num%10)
                num=num//10
                n-=1
            res.extend(tmp[::-1])
        return res
