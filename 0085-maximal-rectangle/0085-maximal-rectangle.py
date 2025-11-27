class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
            heights = heights + [0]
            stack = [] 
            max_area = 0

            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    idx, height = stack.pop()
                    max_area = max(max_area, height * (i - idx))
                    start = idx
                stack.append((start, h))

            return max_area

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            max_area = max(max_area,largestRectangleArea(heights))

        
        return max_area
                



        