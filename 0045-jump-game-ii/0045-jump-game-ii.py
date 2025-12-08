class Solution:
    def jump(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [i for i in range(m)]



        for i in range(m):
            for j in range(1, min(nums[i] + 1, m - i)):
                dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[-1]
        
        

        
        
        


        