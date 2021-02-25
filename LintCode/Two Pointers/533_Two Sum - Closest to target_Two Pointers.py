class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
    
        # Check 
        if len(nums) < 2:
            return 0
            
        # Sort 
        nums.sort()
        
        # Two Pointers
        left, right = 0, len(nums) - 1 
        diff = abs(target - nums[0] - nums[-1])
        while left < right:
            if nums[left] + nums[right] == target:
                return 0
            elif nums[left] + nums[right] > target:
                diff = min(diff, abs(target - nums[left] - nums[right]))
                right -= 1 
            else:
                diff = min(diff, abs(target - nums[left] - nums[right]))
                left += 1 
                
        return diff