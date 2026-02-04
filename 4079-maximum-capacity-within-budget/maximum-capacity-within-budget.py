class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        store = sorted(zip(costs, capacity))
        print(store)
        l=0
        r=len(store)-1
        maxi=0
        ans=0
        while l<=r:
            while l<r and store[l][0]+store[r][0]<budget:
                ans=max(ans,maxi+store[l][1])
                maxi=max(store[l][1],maxi)
                l+=1
            if store[r][0]<budget:
                ans=max(ans,maxi+store[r][1])
            r-=1
        return ans

