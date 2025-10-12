class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        columns = [set()  for _ in range(9)]
        boxes = [set()  for _ in range(9)]

        empty_list = []

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    empty_list.append(i*9 + j)
                else:
                    columns[j].add(val)
                    rows[i].add(val)
                    boxes[(i //3)*3 + j//3].add(val)
        

        
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
                    columns[column_index].add(num)
                    rows[row_index].add(num)
                    boxes[box_index].add(num)
                    board[row_index][column_index] = num


                    if backtrack(pos + 1):
                        return True

                    else:
                        columns[column_index].remove(num)
                        rows[row_index].remove(num)
                        boxes[box_index].remove(num)

            return False 

        backtrack(0)


