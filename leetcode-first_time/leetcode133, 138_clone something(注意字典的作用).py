# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dic = {None:None}
    def cloneGraph(self, node):
        if node == None:
            return
        
        head = UndirectedGraphNode(node.label)
        self.dic[node] = head
        for n in node.neighbors:
            if n in self.dic:
                head.neighbors.append(self.dic[n])
            else:
                neigh = self.cloneGraph(n)
                head.neighbors.append(neigh)
        return head
####------copy undirected graph
    
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def __init__(self):
        self.dic = {}
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return 
        copy = RandomListNode(head.label)
        self.dic[head] = copy
        
        if head.next in self.dic:
            copy.next = self.dic[head.next]
        else:
            copy.next = self.copyRandomList(head.next)
        
        if head.random in self.dic:
            copy.random = self.dic[head.random]
        else:
            copy.random = self.copyRandomList(head.random)
        
        return copy
#--------copy list



            
        
