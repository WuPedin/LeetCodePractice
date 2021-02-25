class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Quick Sort
        def quickSort(left, right):
            # Select pivot
            if left >= right: return
            l, r = left, right
            mid = (r - l) // 2 + l
            pivot = nums[mid]
            
            # Partition
            while r >= l:
                while r >= l and nums[l] < pivot: l += 1
                while r >= l and nums[r] > pivot: r -= 1
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            quickSort(left, r)
            quickSort(l, right)
            
        quickSort(0, len(nums) - 1)
    
        return nums
                
            
            
        
        