class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # Check
        if len(nums) < 2:
            return 0
        
        # Binary Search
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid + 1]:
                start = mid
            elif nums[mid] < nums[mid - 1]:
                end = mid
            else:
                return mid
                
        if nums[start] < nums[end]:
            return end 
        else:
            return start
        