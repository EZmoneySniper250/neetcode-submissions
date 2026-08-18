from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force is to sort all the two strings and compare the string one by one, this will be O(nlogn * n^2) complexity, since the python sort + the nested loop)
        #1. using the dictionary to count the occurances, similar to collections.Counter
        if len(s)!= len(t):
            return False
        ans = defaultdict(int)
        for s_l in s:
            ans[s_l]+=1
        for t_l in t:
            if t_l not in t:
                return False
            ans[t_l]-=1
        return all(ans[x]==0 for x in ans.keys())

