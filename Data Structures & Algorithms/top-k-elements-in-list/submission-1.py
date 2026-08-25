class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        ans = []
        for nums, cnt in count.items():
            ans.append([cnt, nums])
        
        ans.sort()
        rslt = []
        while len(rslt) < k:
            rslt.append(ans.pop()[1])
        
        return rslt

        