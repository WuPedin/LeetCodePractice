class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        
        # Check
        if len(nums) == 1:
            return nums
        
        left, right = 0, 0  # For next non-zero and next zero
        # Find non-zeros and replace to front part
        while right < len(nums):
            
            if nums[right] != 0:
                if left != right:
                    nums[left] = nums[right] # Donnot exchange, cuz we want to minimize number of operations
                left += 1 
            right += 1 
            
        # Fill zeros into back part
        while left < len(nums):
            if nums[left] != 0:
                nums[left] = 0
            left += 1
            
        return nums