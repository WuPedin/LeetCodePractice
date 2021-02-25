class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        
        # Find the first number larger than k 
        right = self.findUpperCloset(A, target)
        left = right - 1 # - 1 cuz target may not exist in the array 
        
        # Put closer number into res array 
        # Back two pointers
        res = []
        for _ in range(k):
            if self.is_left_closer(A, left, right, target):
                res.append(A[left])
                left -= 1 
            else:
                res.append(A[right])
                right += 1 
        return res
        
        
    def findUpperCloset(self, A, target):
        # Binary Search
        # Put <= k on the left side, > k on the right side => find the last target
        start, end = 0, len(A) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] <= target:
                start = mid + 1 
            elif A[mid] > target:
                end = mid
        
        if A[start] >= target:
            return start        
        if A[end] >= target:
            return end 

        # If cannot find 
        return len(A)
                
    
    
    def is_left_closer(self, A, left, right, target):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
