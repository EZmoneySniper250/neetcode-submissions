class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = 0
        while left<=right:
            rate, totaltime = (left + right)//2, 0
            for p in piles:
                totaltime += (p+rate-1)//rate #Equivalent to math.ceil(p, rate)
            if totaltime <= h : ##if smaller or equal to h, it's always within the boundary
                ans = rate
                right  = rate-1 #Since it's already fast, find smaller ones --> decrease the high
            else:
                left = rate +1 #Since it's not enough, find bigger ones -->increase low
        return ans






        