class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path, ans = [], []
        n = len(nums)

        def dfs(start):
            if sum(path) == target:
                ans.append(path.copy()) 
            if sum(path) > target:
                return    
            for j in range(start, n):

                path.append(nums[j])
                dfs(j)
                path.pop()
        
        dfs(0)
        return ans