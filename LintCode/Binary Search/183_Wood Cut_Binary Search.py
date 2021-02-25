class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        
        # Check
        if not L:
            return 0
        
        start, end = 1, min(max(L), sum(L) // k)
        # Weird k
        if start > end:
            return 0
            
        # Binary search    
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_pieces(L, mid) >= k:
                start = mid
            else:
                end = mid
                
        if self.get_pieces(L, end) >= k:
            return end
        if self.get_pieces(L, start) >= k:
            return start
            
        return 0
        
    def get_pieces(self, L, piece_length):
        return sum(l // piece_length for l in L)