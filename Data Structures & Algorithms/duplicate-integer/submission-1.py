class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        pre = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[pre]:
                return True
            else: pre = i
        return False