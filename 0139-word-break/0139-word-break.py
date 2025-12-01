class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        
        dp = [False for _ in range(length+1)]
        dp[0] = True

        for i in range(1,length+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        
        return dp[-1]
            




        