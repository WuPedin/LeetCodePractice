class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
            # Find the first number larger than k 
        right = self.findUpperCloset(arr, x)
        left = right - 1 # - 1 cuz x may not exist in the array 
        
        # Put closer number into res array 
        # Back two pointers
        res = []
        for _ in range(k):
            if self.is_left_closer(arr, left, right, x):
                res.append(arr[left])
                left -= 1 
            else:
                res.append(arr[right])
                right += 1 
        return sorted(res)
        
        
    def findUpperCloset(self, arr, x):
        # Binary Search
        # Put <= k on the left side, > k on the right side => find the last x
        start, end = 0, len(arr) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] <= x:
                start = mid + 1 
            elif arr[mid] > x:
                end = mid
        
        if arr[start] >= x:
            return start        
        if arr[end] >= x:
            return end 

        # If cannot find 
        return len(arr)
                
    
    
    def is_left_closer(self, arr, left, right, x):
        if left < 0:
            return False
        if right >= len(arr):
            return True
        return x - arr[left] <= arr[right] - x
        