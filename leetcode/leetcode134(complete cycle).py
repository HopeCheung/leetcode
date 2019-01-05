class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        def cycle(gas, cost, point):
            store, count, i = gas[point], 1, point
            while count < len(gas) and store >= 0:
                if i != len(gas) - 1:
                    store = store - cost[i]
                    if store < 0:
                        return False
                    store = store + gas[i+1]
                    i = i + 1
                else:
                    store = store - cost[i]
                    if store < 0:
                        return False
                    store = store + gas[0]
                    i = 0
                count = count + 1
            
            if point == 0:
                return store >= cost[len(cost) - 1]
            return store >= cost[point-1] 
                        
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                if cycle(gas, cost, i):
                    return i
        return -1
#-----------time exceeded
class Solution2(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0 or sum(gas) < sum(cost):
            return -1
        
        store, gap, point = 0, 0, 0
        for i in range(len(gas)):
            store = store + gas[i]
            if store >= cost[i]:
                store = store - cost[i]
            else:
                gap = gap + cost[i] - store
                point = i + 1
                store = 0
                
        if point == len(gas) or store < gap: 
            return -1
        return point

                

