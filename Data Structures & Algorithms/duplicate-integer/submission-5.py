class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = dict()
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                return True
        return False