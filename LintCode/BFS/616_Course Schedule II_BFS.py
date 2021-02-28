class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        
        # Get prerequisites of a specific course and the degrees need to take for a specific course
        pre_courses = {i:[] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            pre_courses[j].append(i)
            degrees[i] += 1

        queue, count = collections.deque([]), 0

        # Courses without prerequisites
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)

        # BFS
        order = []
        while queue:
            course = queue.popleft()
            count += 1
            order.append(course)

            for c in pre_courses[course]:
                degrees[c] -= 1
                if degrees[c] == 0:
                    queue.append(c)

        if count == numCourses:
            return order
        return []