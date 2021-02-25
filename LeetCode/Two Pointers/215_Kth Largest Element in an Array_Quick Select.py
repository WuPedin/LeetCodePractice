from random import uniform
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Kth largest = (n - k)th smallest
        k = len(nums) - k
        
        def quick_select(nums, k):
            # Ranfom pick pivot
            pivot = int(uniform(0, len(nums)))
            l, r = [], []
            for i, n in enumerate(nums):
                # Don't put pivot into left
                if n <= nums[pivot] and i != pivot: l.append(n)
                if n > nums[pivot]: r.append(n)
                    
            if k == len(l):
                return nums[pivot]
            elif k < len(l):
                return quick_select(l, k)
            else:
                return quick_select(r, k - len(l) - 1)
            
        return quick_select(nums, k)