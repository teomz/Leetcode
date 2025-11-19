class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows, zero_cols = (
            {j for i in range(len(matrix[0])) for j in range(len(matrix)) if matrix[j][i] == 0},
            {i for i in range(len(matrix[0])) for j in range(len(matrix)) if matrix[j][i] == 0}
        )

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if j in zero_rows or i in zero_cols:
                    matrix[j][i] = 0

        return matrix
        


        