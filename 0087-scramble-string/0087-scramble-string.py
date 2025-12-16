class Solution:
    def __init__(self):
        self.mp = {}
    def isScramble(self, s1: str, s2: str) -> bool:
        m = len(s1)

        if s1 == s2:
            return True

        if s1 == 1:
            return False

        key = s1 + ' ' + s2

        if key in self.mp:
            return self.mp[key]

        for i in range(1,m):
            if self.isScramble(s1[i:],s2[i:]) and self.isScramble(s1[:i],s2[:i]):
                self.mp[key] = True
                return True

            if self.isScramble(s1[i:],s2[:m-i]) and self.isScramble(s1[:i],s2[m-i:]):
                self.mp[key] = True
                return True

        self.mp[key] = False
        return False
        