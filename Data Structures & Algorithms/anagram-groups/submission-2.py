class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)
        for s in strs:
            cnt = [0]*26
            for l in s:
                cnt[ord(l) - ord('a')] +=1
            ans[tuple(cnt)].append(s)
        return list(ans.values())


        