class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        
        results = []
        # Check
        if not nums:
            return [[]] 

        # DFS
        nums.sort()
        self.dfs(nums, 0, [], results)
        return results

    def dfs(self, nums, start_idx, subset, results):
        results.append(subset.copy())

        for i in range(start_idx, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            subset.pop()