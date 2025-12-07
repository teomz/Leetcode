class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def match(i,j):
            return j>=0 and s[i] == p[j] or p[j] == '.'


        m = len(s)
        n = len(p)

        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True


        for j in range(n):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j-1]

        for i in range(m):
            for j in range(n):
                if p[j] == '*':
                    doRepeat = match(i,j-1) and dp[i][j+1]
                    noRepeat = dp[i+1][j-1]
                    dp[i+1][j+1] = doRepeat or noRepeat 
                    continue
                else:
                    dp[i+1][j+1] = match(i,j) and dp[i][j]

        print(dp)
        return dp[m][n]