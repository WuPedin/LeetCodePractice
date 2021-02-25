class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Merge Sort
        # Suitable for devide and conquer
        # Suitable for merging mutiple sorted arrays
        # Suitable for using O(nlogn) algorithm
        # Not suitable for in-place
        # Two parts:
        # 1.  Devide into 2 parts and sort(l), sort(r
        # 1.5 If len = 1, it is sorted
        # 2.  Merge sorted parts
        
        # Devide and sort, O(logn)
        if len(nums) > 1:
            mid = len(nums) // 2
            l = nums[mid:]
            r = nums[:mid]
                     
            self.sortArray(l)
            self.sortArray(r)

            # Merge, O(n)
            i = j = k = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    nums[k] = l[i]
                    i += 1
                else:
                    nums[k] = r[j]
                    j += 1
                k+=1

            # len(l) may be different from len(r), check it
            while i < len(l):
                nums[k] = l[i]
                i += 1
                k += 1
            while j < len(r):
                nums[k] = r[j]
                j += 1
                k += 1
        return nums

        