class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        
        # Count
        pos, neg = 0, 0
        for i in A:
            if i > 0:
                pos += 1 
            else:
                neg += 1
                
        self.partition(A, pos > neg)
        self.interleave(A, pos == neg)
        
        return A
        
        
    # Partition
    def partition(self, A, pos_largerthan_neg):
        
        # Flag to determine pos or neg to put on front
        pos_front = 1 if pos_largerthan_neg else -1

        # Exchange
        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] * pos_front > 0:
                left += 1
            while left <= right and A[right] * pos_front < 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1 
                right -= 1
    
    # Interleave
    def interleave(self, A, is_same_length):
        left, right = 1, len(A) - 1 
        if is_same_length:
            right = len(A) - 2
            
        while left < right:
            A[left], A[right] = A[right], A[left]
            left += 2
            right -= 2
