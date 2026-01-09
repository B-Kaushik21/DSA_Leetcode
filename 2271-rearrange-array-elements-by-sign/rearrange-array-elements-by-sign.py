class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos=[]
        neg=[]
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)

        res = []
        i = 0
        while i < len(pos) or i < len(neg):
            if i < len(pos):
                res.append(pos[i])
            if i < len(neg):
                res.append(neg[i])
            i += 1
        return res