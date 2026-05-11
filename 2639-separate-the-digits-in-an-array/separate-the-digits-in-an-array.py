class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        new=''
        for num in nums:
            new+=str(num)
        #print(new)
        res=[]
        for x in new:
            res.append(int(x))
        return res