class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        list_s = list(s)

        while l < r:
            left =  list_s[l]
            right = list_s[r]
            if left in vowels and right in vowels:
                list_s[l] = right
                list_s[r] = left
                l+=1
                r-=1

            if left not in vowels:
                l+=1
            if right not in vowels:
                r-=1
        

        return "".join(list_s)