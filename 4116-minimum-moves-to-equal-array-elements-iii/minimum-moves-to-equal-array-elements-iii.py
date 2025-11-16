class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi=max(nums)
        count=0
        for num in nums:
            while num!=maxi:
                num=num+1
                count+=1
        return count
            