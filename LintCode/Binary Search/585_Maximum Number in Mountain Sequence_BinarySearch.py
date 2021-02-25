class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        
        return self.binarySearch(nums)
            
    def binarySearch(self, nums):
        
        # End condition
        if len(nums) < 3:
            return max(nums)
        
        # Two pointers
        start, end = 0, len(nums) - 1 
        mid = (start + end) // 2
        
        # Mountaion type
        if nums[start] < nums[mid] and nums[mid] < nums[end]:
            return self.binarySearch(nums[mid:])
        elif nums[start] > nums[mid] and nums[mid] > nums[end]:
            return self.binarySearch(nums[:mid + 1])
        else:
            left = self.binarySearch(nums[:mid + 1])
            right = self.binarySearch(nums[mid:])
            return max(left, right)