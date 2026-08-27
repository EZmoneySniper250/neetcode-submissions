class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        seen = set()
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            diff = 0 - nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] == diff:
                    ans.add(tuple([nums[i], nums[left], nums[right]]))
                    left +=1
                    right -=1
                elif nums[left]+ nums[right] < diff:
                    left +=1
                else: right -=1
        return [list(x) for x in ans]