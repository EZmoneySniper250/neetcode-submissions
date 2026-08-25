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

        # first look through all the cnts
        count = defaultdict(int)
        for n in nums:
            count[n] +=1
        
        freq = [[] for _ in range(len(nums) + 1)] # since occurances should be index, and should be 1 more than indices (fix On space)
        for key, val in count.items():
            freq[val].append(key)
        ans = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
