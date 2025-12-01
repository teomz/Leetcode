class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        nums.sort()
        nums = nums + [0]
        while i < len(nums)-1:
            print(i)
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]

