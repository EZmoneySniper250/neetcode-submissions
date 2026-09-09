class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left, right, maxp = 0,1,0
        # while right<len(prices):
        #     if prices[left]<=prices[right]:
        #         maxp = max(maxp, prices[right] - prices[left])
        #         right +=1
        #     else:
        #         left = right
        # return maxp

        minbuy, maxp = prices[0], 0
        for p in prices:
            minbuy = min(p, minbuy)
            maxp = max(maxp, p-minbuy)
        return maxp
        