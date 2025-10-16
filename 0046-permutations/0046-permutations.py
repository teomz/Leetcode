class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        output.append(nums)
        def backtrack(combi):

            if len(combi) == len(nums):
                if combi not in output:
                    output.append(combi[:])

            for i in range(len(nums)):
                if nums[i] not in combi:
                    combi.append(nums[i])
                    backtrack(combi)
                    combi.pop()
                
        
        backtrack([])
        return output



        