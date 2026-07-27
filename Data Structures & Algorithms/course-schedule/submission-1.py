class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for prereq in prerequisites:
            courseMap[prereq[0]].append(prereq[1])

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if course not in courseMap or courseMap[course] == []:
                return True
            visited.add(course)

            for prereq in courseMap[course]:
                if not dfs(prereq):
                    return False
            courseMap[course] = []
            visited.remove(course)
            return True


        for course in courseMap:
            if not dfs(course):
                return False

        return True

