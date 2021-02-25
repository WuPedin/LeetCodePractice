class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # Check
        if not nums:
            return 0
        
        # Sort 
        nums.sort()
        
        # Two Pointers: nums[l] + nums[r] == target?
        l, r = 0, len(nums) - 1
        ans = []
        while l < r:
            if nums[l] + nums[r] == target:
                if len(ans) == 0:
                    ans.append((nums[l], nums[r]))
                elif len(ans) > 0 and (nums[l], nums[r]) != ans[-1]:
                    ans.append((nums[l], nums[r]))
                l += 1 
                r -= 1 
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
        return len(ans)