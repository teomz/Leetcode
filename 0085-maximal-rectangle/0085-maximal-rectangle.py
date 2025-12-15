class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxArea(heights):
            heights = heights + [0]
            total = 0
            stack = []
            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    idx,height = stack.pop()
                    total = max(total,(i-idx)*height)
                    start = idx

                stack.append((start,h))


            return total


        m = len(matrix)
        n = len(matrix[0])
        dp = [0 for i in matrix[0]]
        maxRec = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[j] = 0
                else:
                    dp[j]+=1

            maxRec = max(maxRec,maxArea(dp))

        return maxRec


        