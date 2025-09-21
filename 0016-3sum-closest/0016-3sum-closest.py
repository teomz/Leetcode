class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        result = 0

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == target:
                    return target

                if abs(current_sum - target) < diff:
                    diff = abs(current_sum - target)
                    result = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result