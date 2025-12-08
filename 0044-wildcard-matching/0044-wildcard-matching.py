class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[False for _ in range(n+1)] for _ in range(m+1)]

        dp[0][0] = True

        for j in range(n):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j]

        
        def match(i,j):
            return j>=0 and s[i] == p[j] or p[j] == '?'


        for i in range(m):
            for j in range(n):
                if p[j] == '*':
                    doRepeat = dp[i][j+1]
                    noRepeat = dp[i+1][j]
                    dp[i+1][j+1] = doRepeat or noRepeat
                else:
                    dp[i+1][j+1] = match(i,j) and dp[i][j]

        return dp[m][n]
        