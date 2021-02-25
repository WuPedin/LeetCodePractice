import functools

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
         
        # Check
        if not s:
            return 0
            
        if len(s) == 1:
            return 1
            
        # Recurrsive
        n = len(s)
        @functools.lru_cache(None)
        def longest_palindrom_subseq_from(i, j):
            if i == j:
                return 1
            if j < i:
                return 0
            if s[i] == s[j]:
                return longest_palindrom_subseq_from(i + 1, j - 1) + 2
            return max(longest_palindrom_subseq_from(i, j - 1), longest_palindrom_subseq_from(i + 1, j))
        
        return longest_palindrom_subseq_from(0, n - 1)
        