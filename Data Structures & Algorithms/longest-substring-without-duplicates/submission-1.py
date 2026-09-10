class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, maxl = 0, 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left +=1
            seen.add(s[right])
            maxl = max(maxl, right+1-left) #index start from 0
        return maxl
        
        