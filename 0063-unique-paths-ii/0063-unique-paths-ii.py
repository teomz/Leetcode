class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0 for _ in range(n)]
        dp[0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                dp[j] = 0 
                break
            else:
                dp[j] = 1



        for i in range(1,m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0 
                    continue
                down = dp[j]
                right = 0
                if j > 0:
                    right = dp[j-1]

                dp[j] = down + right


        return dp[n-1]

                
