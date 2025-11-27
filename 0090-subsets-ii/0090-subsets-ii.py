class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        def backtrack(start,temp):
            if temp not in output:
                output.append(temp[:])
            for i in range(start,len(nums)):
                if nums[i] == nums[i-1] and i > start:
                    continue
                temp.append(nums[i])
                backtrack(i+1,temp)
                temp.pop()
            
        
        backtrack(0,[])
        return output

        