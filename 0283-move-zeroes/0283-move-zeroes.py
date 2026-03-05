class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l= 0
        r = 1
        while l < r and r< len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l] = nums[r]
                nums[r] = 0
                l+=1
                r=l
            if nums[l] != 0:
                l+=1
            r+=1

        return nums
