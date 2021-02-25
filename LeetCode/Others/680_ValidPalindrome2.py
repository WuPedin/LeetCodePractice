class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        """
        is_palinderom(s, left, right)
        left, right = find_difference(s, left, right) -> to find index which is not polindrom
        1. left, right = find_difference(s, left, right)
            if left >= right:
                return True
            else:
                return is_palinderom(s, left + 1, right) or is_palinderom(s, left, right - 1)
        """
        
        # Check
        if not s:
            return -1
        
        # Two Pointers
        left, right = 0, len(s) - 1
        left, right = self.find_difference(s, left, right)
        if left >= right:
            return True
            
        return self.is_palinderom(s, left + 1, right) or self.is_palinderom(s, left, right - 1)
        
    def is_palinderom(self, s, left, right):
        left, right = self.find_difference(s, left, right)
        if left >= right:
            return True
        else:
            return False
        
        
    def find_difference(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right