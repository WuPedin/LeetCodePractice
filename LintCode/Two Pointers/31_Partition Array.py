class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # Check
        if not nums:
            return 0
        
        # Partition
        l, r = 0, len(nums) - 1
        while r >= l:
            while r >= l and nums[l] < k: l += 1
            while r >= l and nums[r] >= k: r -= 1
            
            if r >= l:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        return l

       
       
