class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res=0
        mask=0
        s=set()
        for i in range(30,-1,-1):
            mask|=(1<<i)
            for num in nums:
                s.add(num & mask)
            cur=res|(1<<i)
            for prefix in s:
                if cur ^ prefix in s:
                    res=cur
                    break
            s.clear()
        return res