class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        new=""
        for num in nums:
            new+=str(num)
        res=0
        for i in range(len(new)):
            if new[i]==str(digit):
                res+=1
        return res