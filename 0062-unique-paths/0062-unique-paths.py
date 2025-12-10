class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(n)]

        for i in range(1,m):
            for j in range(n):
                down = dp[j]
                right = 0
                if j>0:
                    right = dp[j-1]
                
                dp[j] = right+down
                
                
        return dp[n-1]