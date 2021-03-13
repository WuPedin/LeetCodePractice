DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        """
        思路
            for矩陣裡的每個字元，確定是否在字典中
            1. 先創造前綴詞的HashMap，紀錄該前綴詞是否為字典中的word
            2. for矩陣裡的每個字元，DFS
        """
        # Check edge case 
        if not words:
            return []
        if not board or len(board) == 0:
            return []
        if not board[0] or len(board[0]) == 0:
            return []

        # Initial
        prefix_is_word = self.get_prefix_set(words)
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        word_set = set()
        
        # DFS
        for i in range(len(board)):
            for j in range(len(board[i])):
                visited[i][j] = True
                self.dfs(board, visited, i, j, prefix_is_word, board[i][j], word_set)
                visited[i][j] = False

        return list(word_set)

    def dfs(self, board, visited, x, y, prefix_is_word, word, word_set):
        if word not in prefix_is_word:
            return 

        # 這裡不return，因為一個word可能是另一個word的前綴詞
        if prefix_is_word[word]:
            word_set.add(word)

        for (dx, dy) in DIRECTIONS:
            next_x = x + dx
            next_y = y + dy

            # 檢查next x, y是否在board中
            if not self.is_valid(board, next_x, next_y) or visited[next_x][next_y]:
                continue

            visited[next_x][next_y] = True
            self.dfs(board, visited, next_x, next_y, prefix_is_word, word + board[next_x][next_y], word_set)
            visited[next_x][next_y] = False

    def is_valid(self, board, x, y):
        return x >= 0 and x < len(board) and y >= 0 and y < len(board[0])

    def get_prefix_set(self, words):
        """
        key放前綴詞，value放是否為word
        """
        prefix_is_word = {}
        for word in words:
            prefix_is_word[word] = True
            for i in range(len(word)):
                prefix = word[:i + 1]
                if prefix not in prefix_is_word:
                    prefix_is_word[prefix] = False 
        return prefix_is_word
                

    