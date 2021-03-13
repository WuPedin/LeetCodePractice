

class DataStream:
    """
    思路
        希望只遍歷一次就可以找到firstUnique
        需要一個LinkedList儲存candidates
        為了實現O(1)查詢，還需要一個HashMap儲存每個需要一個LinkedList儲存candidates的ListNode的位置(其實是存它上個node的記憶體位置)
    """

    def __init__(self):
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.num_to_prev = {}
        self.duplicates = set()
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        if num in self.duplicates:
            return 

        if num not in self.num_to_prev:
            self.push_back(num)
            return

        # Duplicates
        self.duplicates.add(num)
        self.remove(num)

    def remove(self, num):
        prev = self.num_to_prev[num]
        del self.num_to_prev[num]
        cur = prev.next 
        prev.next = cur.next
        
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            self.tail = prev
        

    def push_back(self, num):
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        if not self.dummy.next:
            return None 
        return self.dummy.next.val