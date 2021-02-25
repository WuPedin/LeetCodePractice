class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        
        # Check
        if not nums:
            return -1
        
        # 思維：右半邊的條件：<=最後一個數，所以令target = nums[-1]，找<=target的第一個數即可
        target = nums[-1]
        start, end = 0, len(nums) - 1 
        
        # Binary search
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                end = mid
            else:
                start = mid
                
        return min(nums[start], nums[end])
