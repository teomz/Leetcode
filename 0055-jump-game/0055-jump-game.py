class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = len(nums)
        furthest = nums[0] 


        for i in range(1,m):
            if i > furthest:
                return False
            furthest = max(furthest,i+nums[i]) 
        return True
                    
                
        