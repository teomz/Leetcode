class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        checked = [[False for i in range(len(board[0]))] for j in range(len(board))]

        def backtrack(i,j,temp):
            output = False
            

            if board[i][j] != word[len(temp)]:
                return False

            temp.append(board[i][j])
            checked[i][j] = True

            if ''.join(temp) == word:
                return True

            if j+1 < len(board[0]) and not output and not checked[i][j+1]: #right
                output = backtrack(i,j+1, temp )
            if j-1 >= 0 and not output and not checked[i][j-1]: #left
                output= backtrack(i,j-1, temp )
            if i+1 < len(board) and not output and not checked[i+1][j]: #down
                output = backtrack(i+1,j, temp)
            if i-1 >= 0 and not output and not checked[i-1][j]: #up
                output = backtrack(i-1,j, temp)

            temp.pop()
            checked[i][j] = False
            

            return output

        for i in range(len(board)):
            
            for j in range(len(board[i])):
                output = backtrack(i,j,[])
                if output:
                    break
            if output:
                break
            
        return output

        