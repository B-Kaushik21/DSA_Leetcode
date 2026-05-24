class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res=[]
        store={}
        for num in nums:
            if num not in store:
                store[num]=1
            elif store[num]<k:
                store[num]+=1
        #print(store)
        for num in nums:
            if store[num]>0:
                res.append(num)
            store[num]-=1
        return res

