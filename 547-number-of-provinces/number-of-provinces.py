class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        adj=[[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
        
        def dfs(node,adj,visited):
            visited[node]=True
            for neighbor in adj[node]:
                if visited[neighbor]==False:
                    dfs(neighbor,adj,visited)

        visited=[False]*n
        count=0
        for i in range(n):
            if visited[i]==False:
                count+=1
                dfs(i,adj,visited)
        return count