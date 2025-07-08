from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_graph = {}
        for course in prerequisites:
            if course[0] in courses_graph:
                courses_graph[course[0]].append(course[1])
            else:
                courses_graph[course[0]] = [course[1]]
        visited = {}
        for num in range(numCourses):
            if not self.canFinishCourse(courses_graph, num, visited):
                return False
        return True

    def canFinishCourse(self, courses_graph, course, visited):
        if course in visited:
            return visited[course]
        visited[course] = False
        if course not in courses_graph:
            visited[course] = True
            return True
        canBeFinished = True
        for dep_course in courses_graph[course]:
            canBeFinished = canBeFinished and self.canFinishCourse(courses_graph, dep_course, visited)
        visited[course] = canBeFinished
        return canBeFinished
