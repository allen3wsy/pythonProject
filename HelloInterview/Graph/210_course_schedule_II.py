from collections import defaultdict, deque

# very similar to 207_course_schedule.py
class Solution:
    def find_order(self, num_courses: int, prerequisites: list[list[int]]) -> list[int]:
        # use tasks as an array to be more generic since tasks can be:
        # tasks = [1, 4, 8] random number list instead of [0, 1, 2]
        tasks = [i for i in range(num_courses)]

        # you can also do this to init:
        # graph = {i:[] for i in range(numCourses)} # create node
        graph = defaultdict(list)  # Or: graph = defaultdict(list[int])
        # Use a dictionary to store in-degrees for generic keys
        in_degree = {task: 0 for task in tasks}

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # The rewritten line for generic keys:
        queue = deque([node for node in in_degree if in_degree[node] == 0])

        result = []
        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        # otherwise there is a cycle
        return result if len(result) == num_courses else []