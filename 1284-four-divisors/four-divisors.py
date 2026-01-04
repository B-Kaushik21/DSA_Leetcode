class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res=[]
        def divisor(num,res):
            d=[]
            for i in range(1,int(sqrt(num))+1):
                if num%i==0:
                    if num//i==i:
                        d.append(i)
                    else:
                        d.append(i)
                        d.append(num//i)
            if len(d)==4:
                res.append(sum(d))
        for num in nums:
            divisor(num,res)
        return sum(res)