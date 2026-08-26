class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #O(n), no nested loop, sort allowed here.
        n_set = set(nums)
        max_length = 0
        for n in n_set:
            if n -1 in n_set:
                continue
            length = 1
            while n + length in n_set:
                length += 1
            max_length = max(max_length,length)
        return max_length
            
        
            
        