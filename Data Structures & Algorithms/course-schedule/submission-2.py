class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereqs = defaultdict(list)
        for course, prereq in prerequisites:
            courseToPrereqs[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if course not in courseToPrereqs or len(courseToPrereqs[course]) == 0:
                return True

            visited.add(course)
            for prereq in courseToPrereqs[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            courseToPrereqs[course] = []
            return True
            

        for course in courseToPrereqs:
            if not dfs(course):
                return False
        return True