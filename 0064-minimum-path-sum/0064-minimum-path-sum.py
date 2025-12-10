class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = grid[0][:]

        for j in range(1,n):
            dp[j] += dp[j-1]

        for i in range(1,m):
            dp[0] += grid[i][0] 
            for j in range(1,n):
                val = grid[i][j]
                down = dp[j]
                right = dp[j-1]

                dp[j] = min(val+down, val+right)

        return dp[-1]


                


        