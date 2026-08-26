class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #O(n), no nested loop, sort allowed here.
        n_set = set(nums)
        ind, max_length = 1,1
        for n in n_set:
            if n -1 in n_set:
                continue
            while n + ind in n_set:
                ind += 1
            max_length = max(max_length,ind)
            ind = 1
        return  0 if not n_set else max_length
            
        
            
        