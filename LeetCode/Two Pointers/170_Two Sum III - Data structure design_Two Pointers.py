class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.nums = []
    
    def add(self, number):
        self.nums.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        if not self.nums:
            return -1
        # Sort 
        self.nums.sort()
        
        # Two Pointers: nums[l] + nums[r] == value?
        l, r = 0, len(self.nums) - 1
        ans = []
        while l < r:
            if self.nums[l] + self.nums[r] == value:
                return True
            elif self.nums[l] + self.nums[r] < value:
                l += 1
            else:
                r -= 1
        return False