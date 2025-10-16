class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(combi):

            if len(combi) == len(nums):
                output.append(combi[:])
                return

            for num in nums:
                if num not in combi:
                    backtrack(combi + [num])

                
        
        backtrack([])
        return output



        