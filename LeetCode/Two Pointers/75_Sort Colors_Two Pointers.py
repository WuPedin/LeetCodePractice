class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Idea:   Put 0 on the left and put all 2 on the right.
                1 automatically be put in the middle.
        """
        
        # Two pointers
        # i to look over whole input 
        # i0, i2: the idx to put the next 0, 2 respectively
        # before i cross i2
        i, i0, i2 = 0, 0, len(nums)  - 1
        while i <= i2:
            # If you see 0, exchange nums[i] and nums[i0]
            if nums[i] == 0:
                nums[i], nums[i0] = nums[i0], nums[i]
                i0 += 1
            # If you see 2, exchange nums[i] and nums[i2]
            if nums[i] == 2:
                nums[i], nums[i2] = nums[i2], nums[i]
                i2 -= 1
                # Since origin nums[i2] may be 2. We need to reduce i to make nums[i] exchangable again
                i -= 1
            i += 1
            
        return nums