class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Two Pointers
        """
        
        # Check
        if not nums or len(nums) < 2:
            return [-1, -1]
        
        # Sort O(nlogn)
        numbers = [(number, index) for index, number in enumerate(nums)]
        numbers.sort()
        
        # Hash O(n)
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left][0] + numbers[right][0] < target:
                left += 1
            elif numbers[left][0] + numbers[right][0] > target:
                right -= 1
            else:
                return sorted([numbers[left][1], numbers[right][1]])
        
        return [-1, -1]
        