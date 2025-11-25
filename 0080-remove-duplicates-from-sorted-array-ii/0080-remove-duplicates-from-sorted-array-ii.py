class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = -1
        left, right = 2, 2
        while right < len(nums):
            if left != right:
                nums[left] = nums[right]
            if nums[left]==nums[left-2]:
                right += 1
            else:
                left  += 1
                right += 1


        return left

            

        

        