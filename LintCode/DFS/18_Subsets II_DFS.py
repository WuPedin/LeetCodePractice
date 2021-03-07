class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        
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
            # [1, 2', 2''] 要找到挑了第2個2，但沒挑第1個2的情況，這樣會跟挑了第1個2但沒挑第2個2時重複，所以這種要continue
            # 條件-1: 跟前一個數一樣
            # 條件-2: i != start_idx時，代表沒挑前一個數
            # i == start_idx，代表有挑前一個數
            # 記得取index再迴圈時，都要加避免out of index的發生
            if i != 0 and nums[i] == nums[i - 1] and i != start_idx:
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            subset.pop()
