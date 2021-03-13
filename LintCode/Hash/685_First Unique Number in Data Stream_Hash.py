
class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """

    def firstUniqueNumber(self, nums, number):

        # Check edge case 
        if number not in set(nums):
            return -1

        # Count
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1

            if num == number:
                break

        # Loop till find the first element whose cnt == 1
        for num in nums:
            if cnt[num] == 1:
                return num
            if num == number:
                break 
        return -1

        
