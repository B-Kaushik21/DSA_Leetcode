class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        def recursive_rotate(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        recursive_rotate(0,n-1)
        recursive_rotate(0,k-1)
        recursive_rotate(k,n-1)
        