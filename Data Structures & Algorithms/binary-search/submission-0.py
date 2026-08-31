class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, mid = 0, len(nums)//2
        if nums[left] == target:
            return left
        elif nums[mid] == target:
            return mid
        elif nums[mid]> target:
            while left< mid:
                if nums[left] == target:
                    return left
                left +=1
        else:
            while mid < len(nums):
                if nums[mid] == target:
                    return mid
                mid+=1
        return -1

        
        