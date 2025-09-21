class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0, len(height)-1
        value = 0
        while left < right:
            value = max(value,min(height[left],height[right]) * (right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1


        return value
