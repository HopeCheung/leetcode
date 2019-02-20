class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people == []:
            return []
        
        res = []
        people = sorted(people, key = lambda elem: (-elem[0], elem[1]))
        print(people)
        for p in people:
            res.insert(p[1], p)
        return res
            

        
        
        
        
        
        
        