class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0:
            return True
        if numCourses == 0:
            return False
        
        in_degree = {}
        for elem in prerequisites:
            in_degree[elem[0]] = 0
            
        for elem in prerequisites:
            if len(elem) == 2:
                in_degree[elem[0]] = in_degree[elem[0]]  + 1
                if elem[1] not in in_degree:
                    in_degree[elem[1]] = 0
        
        queue = [u for u in in_degree if in_degree[u] == 0]
        if len(queue) == 0:
            return False
        
        stack = []
        while queue:
            u = queue.pop()
            stack.append(u)
            for elem in prerequisites:
                if elem[1] == u:
                    in_degree[elem[0]] = in_degree[elem[0]] - 1
                    if in_degree[elem[0]] == 0:
                        queue.append(elem[0])
        if 1 in in_degree.values():
            return False
        return len(stack) <= numCourses 
###------https://blog.csdn.net/qq_35644234/article/details/60578189