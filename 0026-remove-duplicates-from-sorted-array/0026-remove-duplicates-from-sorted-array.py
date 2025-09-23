class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left,right = 0,0
        k = 1
        prev = nums[0]
        while right < len(nums):
            if right < 1:
                right += 1
                left += 1
                continue
            if nums[right] == prev:
                right += 1
                continue
            nums[left] = nums[right]
            prev = nums[left]
            left += 1
            right += 1
            k+= 1
        return k
            

        # print(nums,k)
        return k

                
        