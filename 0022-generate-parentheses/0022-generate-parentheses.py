class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        temp = []
        def backtrack(l,r,temp):
            if l == 0 and r == 0:
                output.append(''.join(temp))
            
            if l > 0:
                temp.append('(')
                backtrack(l-1,r,temp)
                temp.pop()

            if l < r:
                temp.append(')')
                backtrack(l,r-1,temp)
                temp.pop()

            
        backtrack(n,n,temp)

        return output


        