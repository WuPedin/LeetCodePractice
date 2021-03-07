class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):

        # Edge case 
        if not nums:
            return [[]]

        # DFS
        permutations = []
        self.dfs(nums, set(), [], permutations)
        return permutations

    # 定義：找到所有permutaiton開頭的permutations
    def dfs(self, nums, visited, permutation, permutations):
        # 出口
        if len(nums) == len(permutation):
            permutations.append(list(permutation))
            return 

        # 拆解
        # [] -> [1] [2] [3] ...
        # [1] -> [1, 2], [1, 3], [1, 4] ...
        for num in nums:
            if num in visited:
                continue
            permutation.append(num)
            visited.add(num)
            self.dfs(nums, visited, permutation, permutations)
            visited.remove(num)
            permutation.pop()