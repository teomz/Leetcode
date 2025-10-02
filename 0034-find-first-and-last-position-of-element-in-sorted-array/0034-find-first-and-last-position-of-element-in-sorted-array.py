class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right = 0, len(nums) -1

        while left <= right:
            mid = (left + right)//2
            print(left,right,mid)
            
            # start with a binary search to find the possible position of target
            if nums[mid] > target:  
                right = mid - 1

            # if found, try to find the left most and right most position 
            elif nums[mid] == target:
                left,right = mid , mid
                while left > 0 and nums[left-1] == target:
                    left = left - 1
                while right < len(nums) -1 and nums[right+1] == target:
                    right = right + 1
                
                return [left,right]

            # else continue with binary search
            else:
                left = mid + 1
                

        return [-1,-1]
            
        