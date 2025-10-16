class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        isUsed = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                output.append(path[:])

            for i in range(len(nums)):
                if i > 0  and nums[i] == nums[i-1] and not isUsed[i-1]:
                    continue
                if not isUsed[i]:
                    isUsed[i] = True
                    backtrack(path + [nums[i]])
                    isUsed[i] = False

        
        backtrack([])
        return output

        