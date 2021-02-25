class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        
        # Quick Select 
        def quickSelect(nums, k):
            
            # Pick pivot
            pivot = len(nums) // 2
            
            # Partition
            l, r = [], []
            for i, num in enumerate(nums):
                if num < nums[pivot]:
                    l.append(num)
                elif num >= nums[pivot] and i != pivot:
                    r.append(num)
                    
            if k == len(l) + 1:
                return nums[pivot] 
            elif k < len(l) + 1:
                return quickSelect(l, k)
            else:
                return quickSelect(r, k - len(l) - 1)
                
        return quickSelect(nums, k)