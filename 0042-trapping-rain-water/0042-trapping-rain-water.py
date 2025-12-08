class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total = 0
        start = 0 

        for ind,h in enumerate(height):
            if stack:
                max_height = stack[0]
            while stack and stack[0] <= h:
                val = stack.pop()
                total += max_height - val
            stack.append(h)

        if stack:
            rev = stack[::-1]
            # rev.append(stack[-1]+1)
            stack = []
            for ind,h in enumerate(rev):
                if stack:
                    max_height = stack[0]
                while stack and stack[0] <= h:
                    val = stack.pop()
                    total += max_height - val
                stack.append(h)


        return total



        