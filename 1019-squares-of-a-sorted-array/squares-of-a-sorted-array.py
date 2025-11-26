class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_nums=[num*num for num in nums]
        squared_nums.sort()
        return squared_nums