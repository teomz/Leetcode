class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = len(nums)
        furthest = nums[0] 


        for i in range(m):
            if i > furthest:
                return False
            furthest = max(furthest,i+nums[i]) 

            if i+nums[i] >= m -1:
                return True
                    
                
        