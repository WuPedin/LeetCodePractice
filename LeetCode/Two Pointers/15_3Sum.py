class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Check
        res = []
        if len(nums) < 3:
            return res
        
        # Sort
        nums.sort()
        
        # Fix a number, and use two pointers to find b + c = -a
        for a in range(len(nums) - 2):
            if a == 0 or (a > 0 and nums[a] != nums[a - 1]):
                l, r, target = a + 1, len(nums) - 1, -nums[a]
                
                while l < r:
                    if nums[l] + nums[r] == target:
                        res.append([nums[a], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1 
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
                    
        
        return res    
S