class LinkedNode:
    """
    LinkedList + HashMap
    """
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None 

class LRUCache:
    """
    @param: capacity: An integer
    """
    """
    思路
        最近被get()或set()的要把它放到最後
        如果新增時capabilit滿了，就把頭的值改掉，然後丟到最後
        用LinkedList + HashMap實現
            LinkedList
                用來表示每個數被訪問的順序，以前 -> 最近
            HashMap
                在Hash中儲存LinkedList的prev Node
                LinkedList = dummy -> 1 -> 2 -> 3 -> null
                Hash[1] = dummy, Hash[2] = node 1
                (prev是因為要增刪查改操作，curr node做不到)
    """
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.key_to_prev = {}
        self.dummy = LinkedNode(0, 0)
        self.tail = self.dummy

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        """
        存在就get，然後移到最後一個
        不存在就return -1
        """
        if key not in self.key_to_prev:
            return -1

        self.move_to_tail(key)
        return self.tail.val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        """
        如果存在就set，然後移到最後一個
        如果不存在就加入
            如果沒超過capacity，就直接加到最後一個
            如果超過，改掉第一個node，然後丟到最後一個，且也要刪除key_to_prev[第一個的key]
        """
        if self.get(key) != -1:
            prev = self.key_to_prev[key]
            prev.next.val = value
            return 

        if self.size < self.capacity:
            self.size += 1
            cur = LinkedNode(key, value)
            self.tail.next = cur
            self.key_to_prev[key] = self.tail
            self.tail = cur
            return 

        first = self.dummy.next 
        del self.key_to_prev[first.key]

        first.key = key
        first.val = value
        self.key_to_prev[key] = self.dummy
        self.move_to_tail(key)

    def move_to_tail(self, key):
        prev = self.key_to_prev[key]
        cur = prev.next

        if self.tail == cur:
            return 

        # 斷掉cur，把cur接到tail
        prev.next = prev.next.next 
        self.tail.next = cur
        cur.next = None 

        # Adjust key_to_prev: 1) prev.next, 2) cur
        if prev.next != None:
            self.key_to_prev[prev.next.key] = prev
        self.key_to_prev[cur.key] = self.tail

        # 改tail指向cur
        self.tail = cur