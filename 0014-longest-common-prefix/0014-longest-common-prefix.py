class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        array = sorted(strs)
        temp = array[0]

        for i in array[1:]:
            for j in range(min(len(i),len(temp))):
                if i[j] != temp[j]:
                    temp = temp[:j]
                    break
        
        return temp



        