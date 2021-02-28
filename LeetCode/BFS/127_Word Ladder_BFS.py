class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Time Complxity: O(n^2 * l^2), for n=# of words, l = size of word
        Space Complexity: O(n)
        """
        queue = collections.deque([beginWord])
        distance = {beginWord: 1}
        mapping = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i] + '*' + word[i + 1:]
                mapping[new_word].append(word)  

        while queue:
            word = queue.popleft()
            if word == endWord:
                return distance[word]

            for next_word in self.get_next_words(word, mapping):
                if next_word in distance:
                    continue
                queue.append(next_word)
                distance[next_word] = distance[word] + 1

        return 0


    def get_next_words(self, word, mapping):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            next_word = left + '*' + right
            if mapping[next_word]:
                words.extend(mapping[next_word])

        return words

        