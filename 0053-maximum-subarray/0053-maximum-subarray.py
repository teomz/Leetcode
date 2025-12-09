class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = len(nums)

        curr = best = nums[0]

        for i in range(1,m):
            curr = max(nums[i],curr+nums[i])
            best = max(curr,best)

        
        return best

        
        