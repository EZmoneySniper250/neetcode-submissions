from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # #brute force is to sort all the two strings and compare the string one by one, this will be O(nlogn ) complexity, since the python sort + the nested loop)
        # #1. using the dictionary to count the occurances, similar to collections.Counter
        # if len(s)!= len(t):
        #     return False
        # ans = defaultdict(int)
        # for s_l in s:
        #     ans[s_l]+=1
        # for t_l in t:
        #     if t_l not in ans:
        #         return False
        #     ans[t_l]-=1
        # return all(ans[x]==0 for x in ans.keys())
        # #The dict method will actually have a time complexity of (O(2n)) and a space complexity of O(n), since there will be a defaultdict created in this case according to the length of the two strings. So I prpose a more efficient way to do this question, by the internal function ord() in python, which returns the ASCII number for each number, here's how it goes

        if len(s)!=len(t):
            return False
        
        cnt = [0]*26 #26 letters, we got O(1) since the length is fixed here, and that's the only list we create here
        for i in range(len(s)):
            #the only loop here --> O(n) in time
            cnt[ord(s[i])-ord('a')] +=1
            cnt[ord(t[i])-ord('a')] -=1
            #if same letter then it's 0 otherwise values exist
        return all(cnt[j] ==0 for j in range(26)) # or all(x == 0 for x in cnt), more pythonic

