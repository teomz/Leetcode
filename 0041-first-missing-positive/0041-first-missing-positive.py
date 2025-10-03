class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        output = 1
        for i in nums:
            if i > 0 and i <= output:
                output += 1
        return output

        