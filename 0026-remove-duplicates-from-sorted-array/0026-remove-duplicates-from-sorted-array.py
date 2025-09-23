class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        idx = 0
        for i in range(len(nums)):
            if i>0 and nums[i] == prev:
                continue
            
            nums[idx] = nums[i]
            prev = nums[idx]
            idx += 1
        return idx

                
        