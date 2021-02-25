class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def quickSort(left, right):
            
            # End condition
            if left >= right:
                return
            
            # Pick pivot 
            l, r = left, right
            mid = (r - l) // 2 + l
            pivot = nums[mid]
            
            # Partition
            while r >= l:
                while r >= l and nums[l] < pivot: l += 1
                while r >= l and nums[r] > pivot: r -= 1
                # Now nums[l] > pivot and nums[r] < pivot. Exchange them
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            # When r <= l, r is new upper bound of left part
            # l is new lower bound of right part
            # Sort these two parts
            quickSort(left, r)
            quickSort(l, right)
            
        quickSort(0, len(nums) - 1)
        return nums