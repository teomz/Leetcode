class Solution:
    def isValid(self, s: str) -> bool:
        m = len(s)

        stack = []
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            elif stack:
                val = stack.pop()
                if val == '(' and i == ')':
                    continue
                elif val == '{' and i == '}':
                    continue
                elif val == '[' and i == ']':
                    continue
                else:
                    return False
            else:
                return False

        if stack:
            return False
        return True
            

        