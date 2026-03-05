class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        i = 0
        merged = ''
        while i<l1 or i<l2:
            if i < l1:
                merged+=word1[i]
            if i <l2:
                merged+=word2[i]
            i+=1

        return merged

        