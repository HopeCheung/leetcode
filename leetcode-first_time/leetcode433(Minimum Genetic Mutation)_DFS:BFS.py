class Solution:
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1
        self.ans = len(bank) + 1
        
        def dfs(curr, path):
            if curr == end:
                self.ans = min(self.ans, len(path))
            else:
                for s in bank:
                    if s not in path and sum([1 for j in zip(curr, s) if j[0] != j[1]]) == 1:
                        path.append(s)
                        dfs(s, path)
                        path.pop()
        dfs(start, [])
        return self.ans if self.ans <= len(bank) else -1
#--------------------------------------DFS-----------------------------------------------------
class Solution:
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1
        queue, bank = [], set(bank)
        queue.append((start, 0))
        
        while len(queue) != 0:
            curr, step = queue.pop(0)
            if curr == end:
                return step
            
            for i in range(len(curr)):
                for c in "ACGT":
                    if curr[:i] + c + curr[i+1:] in bank:
                        bank.remove(curr[:i] + c + curr[i+1:])
                        queue.append((curr[:i] + c + curr[i+1:], step+1))
        return -1
#-------------------------------BFS--------------------------------------------
            
        
        
        