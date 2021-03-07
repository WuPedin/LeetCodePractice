"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # Initialization
        # Capacity = len(hashTable)
        HASH_SIZE = 2 * len(hashTable)
        res_hashTable = [None for _ in range(HASH_SIZE)]

        # Add items
        for item in hashTable:
            p = item
            while p != None:
                self.add_node(res_hashTable, p.val)
                p = p.next

        return res_hashTable

    # 根據hash function去找該加入哪串linkedList
    def add_node(self, res_hashTable, number):
        p = number % len(res_hashTable)
        if res_hashTable[p] == None:
            res_hashTable[p] = ListNode(number)
        else:
            self.add_list_node(res_hashTable[p], number)

    # 在某串linkedList上加入新node
    def add_list_node(self, node, number):
        if node.next != None:
            self.add_list_node(node.next, number)
        else:
            node.next = ListNode(number)