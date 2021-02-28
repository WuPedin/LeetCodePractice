class Solution:
    """
    @param numCourses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):

        # Check 
        if numCourses == 0 or not prerequisites:
            return True 
        
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
        while queue:
            course = queue.popleft()
            count += 1

            for c in pre_courses[course]:
                degrees[c] -= 1
                if degrees[c] == 0:
                    queue.append(c)

        return count == numCourses

