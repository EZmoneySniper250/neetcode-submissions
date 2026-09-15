class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initializing
        ans, left = 0, 0
        max_l = 0
        count = Counter()

        for right in range(len(s)):
            count[s[right]] += 1
            max_l = max(max_l, count[s[right]])
            while right - left + 1 - max_l > k:
                count[s[left]] -= 1
                left += 1
            ans = max(right-left + 1, ans)
        return ans


        