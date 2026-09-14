class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #sliding window
        left = 0
        target, window = Counter(t), Counter()
        need, have  = len(target), 0
        ans_range, min_l = [-1, -1], len(s) + 1
        for right in range(len(s)):
            entry = s[right]
            window[entry] += 1
            if entry in target and window[entry] == target[entry]:
                have += 1
            # delete the entries while have == need
            while have == need:
                cur_l = right - left + 1
                #if smaller than the global minimum then it is the newer global minimum
                if cur_l < min_l:
                    ans_range = [left, right]
                    min_l = cur_l
                term = s[left]
                window[term] -= 1
                if term in target and window[term] < target[term]:
                    have -= 1
                left += 1
        return s[ans_range[0]: ans_range[1]+1] if min_l != len(s) + 1 else ""
            


            
                
