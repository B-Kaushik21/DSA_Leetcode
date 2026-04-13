class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res=[]
        for num in matrix:
            res.append(sum(num))
        return res