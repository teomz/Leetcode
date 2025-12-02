class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        output = ""

        for i in range(n):
            for j in range(i + 1):
                substring = s[j:i+1]
                if substring == substring[::-1]:
                    # Update output only if longer than current longest
                    if len(substring) > len(output):
                        output = substring

        return output
