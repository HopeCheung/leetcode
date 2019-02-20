#leetcode39
class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        if candidates == []:
            return []
        res = []
        
        def helper(begin, target, path):
            if target == 0:
                res.append(path)
                return
            if target < 0 or begin >= len(candidates):
                return
            for i in range(begin, len(candidates)):
                helper(i ,target-candidates[i], path+[candidates[i]])
                
        helper(0, target, [])
        return res

#leetcode40
class Solution2(object):
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        
        def helper(begin, path, target):
            if target == 0:
                if path not in result:
                    result.append(path)
                return
            elif target < 0:
                return
            else:
                for i in range(begin, len(candidates)):
                    helper(i+1, path+[candidates[i]], target - candidates[i])
        helper(0, [], target)   
        return result
            
        