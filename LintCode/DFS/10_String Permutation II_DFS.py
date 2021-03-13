class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        chars = sorted(list(str))
        visited = [False] * len(str)
        permutations = []
        self.dfs(chars, visited, [], permutations)
        return permutations


    def dfs(self, chars, visited, permutation, permutations):
        # 出口
        if len(chars) == len(permutation):
            permutations.append(''.join(permutation))
            return 

        for i in range(len(chars)):
            # 同一個位置上的字不能重複用
            if visited[i]:
                continue

            # a' a" b (V)
            # a" a' b (X)
            # 取第一個當代表，不能跳過第一個a取之後的a
            if i > 0 and chars[i] == chars[i - 1] and not visited[i - 1]:
                continue 

            visited[i] = True 
            permutation.append(chars[i])

            # 找到所有permutation開頭的陣列
            # 找所有a"開頭的
            self.dfs(chars, visited, permutation, permutations)
            # 回溯
            permutation.pop()
            visited[i] = False

        
