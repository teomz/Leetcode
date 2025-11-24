class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            if target <= matrix[i][-1] and target >= matrix[i][0]:
                left,right = 0, len(matrix[i]) -1
                while left <= right:
                    if matrix[i][left] == target or matrix[i][right] == target:
                        return True
                    elif matrix[i][left] < target:
                        left += 1
                    else:
                        right-=1
                    

        return False