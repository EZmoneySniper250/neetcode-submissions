class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            d = target - nums[i]
            if d in seen:
                return [seen[d],i]
            seen[nums[i]] = i
        