class Solution:
    """
    609. Two Sum - Less than or equal to target
    
    Examples: 
        Input:
            [2,7,11,15]
            24
        Output:    
            5
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    
    """
    def twoSum5(self, nums, target):
        
        # Check
        if not nums or len(nums) < 2:
            return 0
        if target is None:
            return -1
        
        # Sort
        nums.sort()
        
        # Two pointers
        cnt = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] <= target:
                cnt += right - left 
                left += 1
            else:
                right -= 1

        return cnt