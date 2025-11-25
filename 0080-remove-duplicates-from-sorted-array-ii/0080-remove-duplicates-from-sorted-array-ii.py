class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = -1
        left, right = 0, 0
        while right < len(nums):
            if left != right:
                nums[left] = nums[right]
            if left >1 and nums[left]==nums[left-1] and nums[left]==nums[left-2]:
                right += 1
            else:
                left  += 1
                right += 1


        return left

            

        

        