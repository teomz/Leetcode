class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = strs[0]
        for i in range(1,len(strs)):
            check = ''
            for j in range(min(len(strs[i]),len(temp))):
                if temp[j] == strs[i][j]:
                    check += temp[j]
                else:
                    break
    
            temp = check
        return temp



        