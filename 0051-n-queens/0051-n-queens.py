class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [False] * n
        diag = [False] * (2*n - 1)
        antidiag = [False] * (2*n - 1)


        res = []

        def backtrack(row,path):
            
            if len(path) == n:
                res.append(path[:])


            for col in range(n):
                if  not cols[col] and not diag[row+col] and not antidiag[row-col+n-1]:
                    cols[col] = True
                    diag[row+col] = True
                    antidiag[row-col+n-1]= True
                    backtrack(row+1,path + [ "."*col + "Q" + "."*(n-col-1)])
                    cols[col] = False
                    diag[row+col] = False
                    antidiag[row-col+n-1]= False

        
        backtrack(0,[])
        print(res)
        return res
            
            




            





