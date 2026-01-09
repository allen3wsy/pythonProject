from collections import deque, defaultdict

def topological_sort(adj_list):
    # 1. Initialize defaultdict
    # Default value will be 0 for any new key accessed
    indegree = defaultdict(int)

    # 2. Populate indegree
    for u in adj_list:
        # CRITICAL STEP: Access the key 'u' to ensure it exists in the map.
        # If 'u' has no incoming edges, this creates it with value 0.
        # If 'u' already exists (from a previous 'v' update), this does nothing.
        indegree[u]

        for v in adj_list[u]:
            indegree[v] += 1

    # 3. Enqueue nodes with indegree 0
    # Now we are safe to iterate indegree because all nodes are registered
    queue = deque([node for node in indegree if indegree[node] == 0])

    order = []
    while queue:
        u = queue.popleft()
        order.append(u)

        if u in adj_list:
            for v in adj_list[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

    return order if len(order) == len(indegree) else []

####
### another way
# indegree = {u: 0 for u in adj_list}
####


def topological_sort(adj_list):
    # 1. Initialize ALL nodes to 0 first
    # This replaces the "critical step" inside the loop
    indegree = {u: 0 for u in adj_list}
    
    # 2. Calculate indegrees
    for u in adj_list:
        for v in adj_list[u]:
            # We can use .get() here to handle nodes that might
            # appear in values but not in keys (sparse graph)
            indegree[v] = indegree.get(v, 0) + 1

    # 3. Enqueue
    queue = deque([u for u in indegree if indegree[u] == 0])

    order = []
    while queue:
        u = queue.popleft()
        order.append(u)

        if u in adj_list:
            for v in adj_list[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

    return order if len(order) == len(indegree) else []




