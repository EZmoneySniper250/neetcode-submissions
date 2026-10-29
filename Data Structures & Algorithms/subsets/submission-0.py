class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, path = [], []
        n = len(nums)

        def dfs(start):
            ans.append(path.copy())
            for j in range(start, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        
        dfs(0)
        return ans
