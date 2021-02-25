class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        
        # Exponential Backoff 倍增法
        kth = 1 
        while reader.get(kth - 1) < target:
            kth *= 2
        
        # Binary search
        start, end = kth // 2, kth - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) < target:
                start = mid + 1 
            else:
                end = mid
                
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end 
            
        return -1