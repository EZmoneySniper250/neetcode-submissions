class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # #dict O(nlogn)
        # count = defaultdict(int)
        # for n in nums:
        #     count[n] += 1
        # ans = sorted(count, key = lambda x: count[x], reverse = True)
        # rslt = []
        # while len(rslt) < k:
        #     rslt.append(ans.pop(0))
        
        # return rslt

        #bucket sort (On)
        cnt = dict()
        for n in nums:
            cnt[n] = cnt.get(n,0) + 1 #or defaultdict
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in cnt.items():
        #freq is a list for storing the nums, its index is the appearance of the nums. Then use reverse loop to output the numbers
            freq[cnt].append(num)
        ans = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
