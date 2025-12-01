class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]+1:
                count += 1
            else:
                count = 1
            if count > max_count:
                max_count = count
        return max_count
        