class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        #first make all the words in the list sorted (Ologn)
        #then iterate through the list (On)
        #Complexity (O(nLogn))
        for s in strs:
            s_n = ''.join(sorted(s))
            ans[s_n].append(s)

        return list(ans.values())