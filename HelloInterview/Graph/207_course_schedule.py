from collections import defaultdict, deque

# Meta
# very similar to 210_course_schedule_II.py
class Solution:
    def can_finish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        # use tasks as an array to be more generic since tasks can be:
        # tasks = [1, 4, 8] random number list instead of [0, 1, 2]
        tasks = [i for i in range(num_courses)]

        # you can also do this to init:
        # graph = {i:[] for i in range(numCourses)} # create node
        graph = defaultdict(list) # Or: graph = defaultdict(list[int])
        # Use a dictionary to store in-degrees for generic keys
        in_degree = {task: 0 for task in tasks}

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # The rewritten line for generic keys:
        queue = deque([node for node in in_degree if in_degree[node] == 0])

        count = 0
        while queue:
            course = queue.popleft()
            count += 1

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        # otherwise there is a cycle
        return count == len(tasks)