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

        prev = self.key_to_prev[key]
        curr = prev.next

        self.kick(prev)
        return curr.val

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
        if key in self.key_to_prev:	   
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.val = value
            return
        
        self.push_back(LinkedNode(key, value))  #如果key不存在，则存入新节点
        if len(self.key_to_prev) > self.capacity:		#如果缓存超出上限
            self.pop_front()					#删除头部
        

    def pop_front(self):
        # 删除头部
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy

    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):    #将数据移动至尾部
        node = prev.next
        if node == self.tail:
            return
        
        # remove the current node from linked list
        prev.next = node.next
        # update the previous node in hash map
        self.key_to_prev[node.next.key] = prev
        node.next = None

        self.push_back(node)