class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        
        # Check
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        # Count
        from collections import Counter
        cnt = Counter(s)
        
        # Find pairs, and we can place 1 un-paired element for center
        longest = 0
        flag1 = 0
        for val in cnt.values():
            if val % 2 == 0:
                longest += val
            else:
                if val >= 3:
                    longest += val - 1
                    flag1 = 1
                if val == 1:
                    flag1 = 1
        
        return longest + flag1