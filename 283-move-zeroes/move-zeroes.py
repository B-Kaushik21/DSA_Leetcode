class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        for i in range(len(nums)): #non-zero elements placed
            if nums[i]!=0:
                nums[count]=nums[i]
                count+=1
        #count here says the non-zero elements
        while (count<len(nums)): # exceed the length of list loop stops
            nums[count]=0
            count+=1
        