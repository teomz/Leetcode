class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtrack(i,temp,output):
            output.append(temp[:])
            for val in range(i,len(nums)):
                temp.append(nums[val])
                backtrack(val+1,temp,output)
                temp.remove(nums[val])
            

            


        backtrack(0,[],output)
        return output
        