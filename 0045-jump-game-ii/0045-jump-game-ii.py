class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        fartest = 0 
        jump = 0
        current = 0

        for i in range(n-1):
            fartest = max(fartest, i+nums[i])
            
            if current == i:
                jump +=1
                current = fartest
            
                if current >= n - 1:
                    break

        return jump

        