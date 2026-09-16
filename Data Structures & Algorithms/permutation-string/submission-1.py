class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #using sliding window to detect the occurances of the strings
        target, window = Counter(s1), Counter()

        #initialization
        left = 0

        for right in range(len(s2)):
            window[s2[right]] += 1
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            if target == window:
                return True
        return False
            
        