class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        
        # Check 
        if len(S) < 3:
            return 0
            
        # Sort 
        S.sort()
        
        # Two pointers
        left, right = 0, len(S) - 1 
        ans = 0
        
        for i in range(2, len(S)):
            left, right = 0, i - 1
            while left < right:
                if S[left] + S[right] > S[i]:
                    ans += (right - left)
                    right -= 1 
                else:
                    left += 1
        
        return ans