class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # 要先去掉重複，再排序
        candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results
        

    def dfs(self, candidates, target, start, combination, results):
        # 從target開始，減成0就可以return了
        if target < 0:
            return 
        if target == 0:
            return results.append(list(combination))

        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            self.dfs(
                candidates,
                target - candidates[i],
                i, # 可以重複選，所以不是i + 1
                combination,
                results
            )
            combination.pop()

