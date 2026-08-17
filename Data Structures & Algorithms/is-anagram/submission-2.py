class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        
        cnt = dict()
        for s_l in s:
            cnt[s_l] = cnt.get(s_l, 0)+1
        for t_l in t:
            if t_l not in s:
                return False
            cnt[t_l] = cnt.get(t_l) -1
            if cnt[t_l] < 0:
                return False
        return True


