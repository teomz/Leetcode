class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        isUsed = [False]* len(nums)

        def backtrack(combi):

            if len(combi) == len(nums):
                output.append(combi[:])
                return

            for i in range(len(nums)):
                if not isUsed[i]:
                    isUsed[i] = True
                    backtrack(combi + [nums[i]])
                    isUsed[i] = False

                
        
        backtrack([])
        return output



        