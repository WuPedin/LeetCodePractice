class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        
        # Check
        if not A:
            return -1
            
        # Check target is on left or right side, but both are rotated sorted array 
        start, end = 0, len(A) - 1 
        while start + 1 < end:
            mid = (start + end) // 2
            
            # -> /   /
            if A[mid] >= A[start]:
                # On left side
                if A[start] <= target <= A[mid]:
                    end = mid
                # On right side
                else:
                    start = mid
            # /    / <-
            else:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid
                    
        if A[start] == target:
            return start
        if A[end] == target:
            return end
            
        return -1