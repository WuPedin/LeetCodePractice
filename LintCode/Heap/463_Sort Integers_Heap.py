class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # 先做一個最大堆積
        self.heapify(A)
        for i in range(len(A) - 1, 0, -1):
            # 第一個已經是最大值
            # 所以丟到最後一個去
            A[0], A[i] = A[i], A[0]
            # 然後再去shift down 0 ~ i-1個數
            self.shiftdown(A, 0, i - 1)

    
    # 最大堆積
    def heapify(self, A):
        for i in range((len(A) - 1) // 2, -1, -1):
            self.shiftdown(A, i, len(A) - 1)

    # 加入end參數，控制堆size越來越小
    def shiftdown(self, A, k, end):
        while k * 2 + 1 <= end:
            son = k * 2 + 1
            # 選最大的兒子
            if k * 2 + 2 <= end and A[son] < A[k * 2 + 2]:
                son = k * 2 + 2

            # 如果兒子大於父親，要交換
            if A[son] <= A[k]:
                break
            A[k], A[son] = A[son], A[k]
            k = son