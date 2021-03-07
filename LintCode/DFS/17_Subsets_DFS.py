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

    # 遞迴的定義
    def dfs(self, nums, idx, subset, results):

        # 遞迴的出口
        if idx == len(nums):
            # 注意! 這裡要深度拷貝
            results.append(subset.copy())
            return  

        # 遞迴的拆解
        # 取nums[idx]
        subset.append(nums[idx])
        self.dfs(nums, idx + 1, subset, results)

        # 不取nums[idx]
        subset.pop()
        self.dfs(nums, idx + 1, subset, results)
