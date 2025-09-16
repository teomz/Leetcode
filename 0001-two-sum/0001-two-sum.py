class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = {}
        for idx, num in enumerate(nums):
            check = target - num
            if check in hmap:
                return [hmap[check], idx] 
            hmap[num] = idx

            
        