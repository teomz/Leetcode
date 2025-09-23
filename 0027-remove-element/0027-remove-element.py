class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[idx] = nums[i]
            idx += 1
        return idx
            


        