class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        store=Counter(nums)
        res=[]
        for key,val in store.items():
            if val==2:
                res.append(key)
        return res


        # arr=[]
        # for i in range(len(nums)):
        #     if nums[i]  in nums[i+1:]:
        #         arr.append(nums[i])
        # return arr
       
        seen=set()
        res=list()

        for i in nums:
            if i in seen:
                res.append(i)
            else:
                seen.add(i)
        return res