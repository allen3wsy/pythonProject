from collections import deque

class Solution:
    def depthSumInverse(self, nestedList: list['NestedInteger']) -> int:
        Q = deque()
        Q.extend(nestedList)

        depth = 1
        max_depth = 0
        sum_of_elements = 0
        sum_of_products = 0

        while Q:
            size = len(Q)
            max_depth = max(max_depth, depth)
            
            for _ in range(size):
                nested = Q.popleft() # Equivalent to Q.poll() in Java

                if nested.isInteger():
                    sum_of_elements += nested.getInteger()
                    sum_of_products += nested.getInteger() * depth
                else:
                    Q.extend(nested.getList())
            depth += 1
            
        return (max_depth + 1) * sum_of_elements - sum_of_products