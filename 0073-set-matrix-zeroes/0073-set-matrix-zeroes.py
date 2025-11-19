class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        changed = [[True if i == 0 else False for i in j] for j in matrix]

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                val = matrix[j][i]
                if max(changed[j]) or  max([boolean[i] for boolean in changed]) :
                    matrix[j][i] = 0

        
        return matrix


        