class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #1 defaultdict list
        # ans = defaultdict(list)
        # #first make all the words in the list sorted (Ologn)
        # #then iterate through the list (On)
        # #Complexity (O(nLogn))
        # for s in strs:
        #     s_n = ''.join(sorted(s))
        #     ans[s_n].append(s)

        # return list(ans.values())

        #2 using ord
        ans = defaultdict(list)
        for s in strs:
            cnt = [0]*26
            for l in s:
                cnt[ord(l)-ord('a')]+=1
            ans[tuple(cnt)].append(s)
        
        return list(ans.values())