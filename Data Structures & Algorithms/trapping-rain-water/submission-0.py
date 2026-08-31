class Solution:
    def trap(self, height: List[int]) -> int:

        #mono stack
        ans = 0
        stack = []
        for i, h in enumerate(height):
            while stack and stack[-1][1] <=h:
                _, mid_h = stack.pop()
                if not stack:
                    break
                ind, left = stack[-1]
                ans += (min(h, left) - mid_h)*(i - ind - 1) #see how many empty spaces can be filled horizontally
            stack.append((i, h))
        return ans
