class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]

        empty_list = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_list.append(i*9 + j)
                else:
                    columns[j].append(board[i][j])
                    rows[i].append(board[i][j])
                    boxes[(i //3)*3 + j//3].append(board[i][j])
        

        
        def backtrack(pos):
            if pos == len(empty_list):
                return True

            index = empty_list[pos]
            
            column_index = index % 9 
            row_index = index // 9
            box_index = (row_index //3)*3 + column_index//3

            for num in range(1,10):
                num = str(num)
                if num not in columns[column_index] and num not in rows[row_index] and num not in boxes[box_index]:
                    columns[column_index].append(num)
                    rows[row_index].append(num)
                    boxes[box_index].append(num)
                    board[row_index][column_index] = num


                    if backtrack(pos + 1):
                        return True

                    else:
                        columns[column_index].pop()
                        rows[row_index].pop()
                        boxes[box_index].pop()

            return False 

        backtrack(0)


