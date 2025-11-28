class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        output = [triangle[0][0]]
        for i in range(1,len(triangle)):
            temp = [output[0] + triangle[i][0]]
            for j in range(1,len(triangle[i])-1):
                val = triangle[i][j]
                temp.append(min(output[j] + val, output[j-1] + val))
            temp.append(output[-1]+triangle[i][-1])
            output = temp


        return min(output)





        