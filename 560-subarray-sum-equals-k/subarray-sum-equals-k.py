class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={}
        res=0
        curr=0
        for num in nums:
            curr+=num
            #if curr==k then new subarray is found
            if curr==k:
                res+=1
            
            #diff exists in prefix dict
            if curr-k in prefix:
                res+=prefix[curr-k]
          #add curr to dict of prefix
            prefix[curr]=prefix.get(curr,0)+1
        return res