class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        
        # Check 
        if not nums:
            return 0
        
        # Sort, O(nlogn)
        nums.sort()
        
        # Two Pointers
        left, right = 0, len(nums) - 1 
        ans = 0
        while left < right:

            if nums[left] + nums[right] > target:
                ans += (right - left)
                right -= 1 
            elif nums[left] + nums[right] <= target:
                left += 1 
                
        return ans
