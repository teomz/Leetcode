class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ''
        m = len(s)
        for i in range(m):
            for j in range(i+1):
                substring = s[j:i+1]
                revstring = substring[::-1]
                if substring == revstring:
                    if len(output) < len(substring):
                        output = substring

        
        return output


