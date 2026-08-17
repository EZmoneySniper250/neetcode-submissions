from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1. using dictionary to count the occurances (manually write the counter)
        # if len(s)!= len(t):
        #     return False
        # cnt = dict()
        # for s_l in s:
        #     cnt[s_l] = cnt.get(s_l,0) +1
        
        # for t_l in t:
        #     if t_l not in cnt:
        #         return False
        #     cnt[t_l] -=1
        #     if cnt[t_l] < 0:
        #         return False
        # return True

        #2 using ord ord(a) is an internal function that
        if len(s)!=len(t):
            return False
        cnt = [0]*26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('a')] +=1
            cnt[ord(t[i]) - ord('a')] -=1
        return all(x == 0 for x in cnt)






