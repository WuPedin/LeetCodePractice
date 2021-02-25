class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Counter
        cnter = {}
        cnter[0], cnter[1] = 0, 0
        for i, num in enumerate(nums):
            if num == 0:
                cnter[0] += 1
            elif num == 1:
                cnter[1] += 1
                
        nums[:] = [0] * cnter[0] + [1] * cnter[1] + [2] * (len(nums) - cnter[0] - cnter[1])
        return nums