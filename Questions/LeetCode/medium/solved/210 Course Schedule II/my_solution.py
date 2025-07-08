from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_graph = {}
        for prereq in prerequisites:
            if prereq[0] in course_graph:
                course_graph[prereq[0]].append(prereq[1])
            else:
                course_graph[prereq[0]] = [prereq[1]]

        completed = {}
        order = []
        for course in range(numCourses):
            if not (self.canFinishCourse(course_graph, course, completed, order)):
                return []
        return order

    def canFinishCourse(self, graph, course, completed, order):
        if course in completed:
            return completed[course]
        completed[course] = False
        if course not in graph:
            order.append(course)
            completed[course] = True
            return True
        canBeFinished = True
        for dep_course in graph[course]:
            canBeFinished = canBeFinished and self.canFinishCourse(graph, dep_course, completed, order)
        completed[course] = canBeFinished
        if canBeFinished:
            order.append(course)
        return canBeFinished