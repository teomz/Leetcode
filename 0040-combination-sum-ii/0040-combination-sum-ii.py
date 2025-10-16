class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(index,target,curr_list):
            if target == 0:                    
                res.append(curr_list[:])
                return
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                curr_list.append(candidates[i])
                if target >= 0 :
                    backtrack(i+1,target-candidates[i],curr_list)

                curr_list.pop()


        backtrack(0,target,[])
        return res