class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        
        # Check
        if len(M) == 0:
            return 0
            
        # Initialize
        res = []
        friend, not_friend, unknown = collections.deque([]), [], collections.deque(range(len(M)))
        
        # Search from first person A
        # Search from person B who is not in friend circle of A
        while unknown:
            circle = []
            i = unknown.popleft()
            circle.append(i)
            
            # Search friends and not_friends of A
            while unknown:
                j = unknown.popleft()
                if M[i][j] == 1:
                    friend.append(j)
                else:
                    not_friend.append(j)
                    
            # Search indirect friends of A
            while friend:
                i = friend.popleft()
                circle.append(i)
                for idx, j in enumerate(not_friend):
                    if M[i][j] == 1:
                        friend.append(j)
                        not_friend.pop(idx)
            
            res.append(circle)
            
            # End condition: no person left
            if len(not_friend) == 0:
                break
            
            unknown = collections.deque(not_friend)
            not_friend = []

        return len(res)
                
        