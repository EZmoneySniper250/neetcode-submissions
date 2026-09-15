class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initializing
        ans, left = 0, 0
        max_l = 0
        count = Counter()

        for right in range(len(s)):
            count[s[right]] += 1
            # max_l here is the length for the maximum string count here, not a single string length
            max_l = max(max_l, count[s[right]])
            # left -> right is the range for all the string, max_l should always be within right -> left, then the remaining part should always be smaller than the maximum replacements. IF exceed then shrink start
            while right - left + 1 - max_l > k:
                count[s[left]] -= 1
                left += 1
            ans = max(right-left + 1, ans)
        return ans


        