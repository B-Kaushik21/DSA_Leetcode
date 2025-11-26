class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        modulo=1000000007
        n, m = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(m)] for _ in range(n)]
        dp[0][0][grid[0][0] % k] = 1
        
        for i in range(n):
            for j in range(m):
                for mod in range(k):
                    if j > 0:
                        dp[i][j][(mod + grid[i][j]) % k] += dp[i][j - 1][mod] % modulo
                    if i > 0:
                        dp[i][j][(mod + grid[i][j]) % k] += dp[i - 1][j][mod] % modulo
        
        return dp[-1][-1][0] % modulo 