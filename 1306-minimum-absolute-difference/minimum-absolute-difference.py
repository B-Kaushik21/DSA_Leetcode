class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        print(arr)
        res=[]
        n=len(arr)
        mini=float('inf')
        for i in range(1,n):
            mini=min(mini,abs(arr[i]-arr[i-1]))
        #print(mini)
        for i in range(n-1):
            if (arr[i+1]-arr[i])==mini:
                res.append([arr[i],arr[i+1]])
        return res