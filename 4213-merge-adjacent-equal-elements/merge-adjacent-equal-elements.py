class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack=[]
        for x in nums:
            while stack and stack[-1]==x:
                x+=stack.pop()
            stack.append(x)
        return stack