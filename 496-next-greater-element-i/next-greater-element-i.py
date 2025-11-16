class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        for target in nums1:
            nge=-1
            target_found=False
            for num in nums2:
                if num==target:
                    target_found=True
                elif target_found:
                    if num>target:
                        nge=num
                        break
            stack.append(nge)
        return stack