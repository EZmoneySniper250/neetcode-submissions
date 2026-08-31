class Solution:
    def trap(self, height: List[int]) -> int:

        # #mono stack
        # ans = 0
        # stack = []
        # for i, h in enumerate(height):
        #     while stack and stack[-1][1] <=h:
        #         _, mid_h = stack.pop()
        #         if not stack:
        #             break
        #         ind, left = stack[-1]
        #         ans += (min(h, left) - mid_h)*(i - ind - 1) #see how many empty spaces can be filled horizontally
        #     stack.append((i, h))
        # return ans

        #pre suf

        # n = len(height)
        # pre = [0] * n
        # suf = [0] * n
        # pre[0] = height[0]
        # suf[n-1] = height[n-1]
        # for i in range(1,n):
        #     pre[i] = max(pre[i-1], height[i])
        # for j in range(n-2, -1, -1):
        #     suf[j] = max(suf[j+1], height[j])
        
        # ans = 0
        # for i in range(n):
        #     ans += min(pre[i], suf[i]) - height[i]
        # return ans

        #two pointer
        n, ans = len(height), 0
        left, right, left_max, right_max = 0, n-1, height[0], height[n-1]
        while left < right:
            if left_max <= right_max:
                left+=1
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                
            else:
                right -=1
                right_max = max(right_max, height[right])
                ans+= right_max - height[right]
                
        return ans

