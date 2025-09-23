class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n,r = len(nums), len(nums) - 2
        while r>= 0 and nums[r] >= nums[r+1]:
            r -= 1
        
        if r== -1:
            nums.reverse()
            return

        i = n - 1
        while nums[i] <= nums[r]:
            i -= 1
        
        nums[r], nums[i] = nums[i], nums[r]

        nums[r+1:] = reversed(nums[r+1:])
        
        