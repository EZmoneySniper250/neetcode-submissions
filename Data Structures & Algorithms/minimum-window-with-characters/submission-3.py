class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # using sliding window, since we need to shrink the window as we met all the requirements
        target, window = Counter(t), Counter()
        #we need to set up the need and have, to see when we can start to shrink the window
        need, have = len(target), 0
        #we also need some global indicators, to 1. record the minimum length 2. record the indices (for preventing overwrite of a longer substring) 3. the left index (for initializing the     shrink after match condition)
        left, min_l, ans_ind = 0, len(s)+ 1, [-1, -1]

        #start looping
        for right in range(len(s)):
            entry = s[right]
            window[entry] += 1
            if entry in target and target[entry] == window[entry]:
                have += 1
            
            #start shrinking
            while need == have:
                cur_l = right - left + 1
                if cur_l < min_l: #global minimum recorded, start updating the answer, otherwise continue
                    min_l = cur_l
                    ans_ind = [left, right]
                window[s[left]] -= 1    
                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                left += 1
        l, r = ans_ind[0], ans_ind[1]
        return s[l:r+1] if min_l != len(s) + 1 else ""


        