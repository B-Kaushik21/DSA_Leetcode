class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # Build tree
        children = [[] for _ in range(n)]
        for u, v in hierarchy:
            children[u - 1].append(v - 1)

        # profit[node][bossBuy]
        profit = [[0, 0] for _ in range(n)]
        for i in range(n):
            profit[i][0] = future[i] - present[i]
            profit[i][1] = future[i] - present[i] // 2

        # dp[node][bossBuy][buy][budget]
        dp = [[[[-10**18] * (budget + 1) for _ in range(2)] for _ in range(2)] for _ in range(n)]

        # visited[node][bossBuy][buy]
        visited = [[[False] * 2 for _ in range(2)] for _ in range(n)]

        def dfs(node: int, bossBuy: int, buy: int):
            if visited[node][bossBuy][buy]:
                return
            visited[node][bossBuy][buy] = True

            cur = [-10**18] * (budget + 1)

            # cost of buying this node
            cost = 0
            if buy:
                cost = present[node] // 2 if bossBuy else present[node]

            if cost <= budget:
                cur[cost] = profit[node][bossBuy] if buy else 0

            # merge children
            for child in children[node]:
                dfs(child, buy, 1)
                dfs(child, 0, 0)

                take = dp[child][buy][1]
                skip = dp[child][0][0]

                merged = [-10**18] * (budget + 1)

                for b in range(budget + 1):
                    if cur[b] == -10**18:
                        continue
                    for x in range(budget - b + 1):
                        best = max(take[x], skip[x])
                        if best != -10**18:
                            merged[b + x] = max(merged[b + x], cur[b] + best)

                cur = merged

            dp[node][bossBuy][buy] = cur

        # root can buy or skip
        dfs(0, 0, 0)
        dfs(0, 0, 1)

        ans = 0
        for b in range(budget + 1):
            ans = max(ans, dp[0][0][0][b], dp[0][0][1][b])

        return ans
