class Node:
    def __init__(self, _val):
        self.next = None
        self.val = _val


class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    
    def __init__(self):
        self.head, self.tail = None, None
        
    def enqueue(self, item):
        
        # Check if full queue 
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    """
    @return: An integer
    """
    def dequeue(self):
        
        # Check
        if self.head is not None:
            item = self.head.val
            self.head = self.head.next
            return item
        else:
            return -1