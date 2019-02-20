class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        G = collections.defaultdict(list)
        for u, v in tickets: 
            G[u].append(v)
            G[u].sort()   
        
        route = []
        def dfs(start):
            while G[start]:
                next_start = G[start].pop(0)
                dfs(next_start)
            route.append(start)

        dfs("JFK")
        return route[::-1]