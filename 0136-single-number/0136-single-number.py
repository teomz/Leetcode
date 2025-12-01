class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        x = 0
        for i in nums:
            x^=i
        return x
