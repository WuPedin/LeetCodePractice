class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        for i in range((len(A) - 1) // 2, -1, -1):
            self.shiftdown(A, i)

    def shiftdown(self, A, k):
        while k * 2 + 1 < len(A):
            son = k * 2 + 1
            # 選最小的兒子
            if k * 2 + 2 < len(A) and A[son] > A[k * 2 + 2]:
                son = k * 2 + 2

            # 如果兒子小於父親，要交換
            if A[son] >= A[k]:
                break
            A[k], A[son] = A[son], A[k]
            k = son