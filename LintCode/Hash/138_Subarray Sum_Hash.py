class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        
        presum_hash = {0: -1}
        presum = 0

        for i, num in enumerate(nums):
            presum += num
            if presum in presum_hash:
                return [presum_hash[presum] + 1, i]
            presum_hash[presum] = i 

        return [-1, -1]