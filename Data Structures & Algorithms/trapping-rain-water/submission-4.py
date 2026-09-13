class Solution:
    def trap(self, height: List[int]) -> int:



        # #two pointer
        # n, ans = len(height), 0
        # left, right, left_max, right_max = 0, n-1, height[0], height[n-1]
        # while left < right:
        #     if left_max <= right_max:
        #         left+=1
        #         left_max = max(left_max, height[left])
        #         ans += left_max - height[left]
                
        #     else:
        #         right -=1
        #         right_max = max(right_max, height[right])
        #         ans+= right_max - height[right]
                
        # return ans

        # Mono stack
        ans , stack = 0, []
        #logic: think about the water is trapped horizontally, we will try to fill in the missing areas according to the height of the bars we are meeting. As the current bar is bigger than the previous one, we can remove the previous one and calcualte the horizontal area and keep so on under we met a higher bar or we just identify the current bar is the highest
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                mid = stack.pop()
                if not stack:
                    break #we will need another boundary
                left = stack[-1]
                dh = min(height[left], h) - height[mid]
                l = i - left - 1
                ans += dh*l
            stack.append(i)
        return ans

