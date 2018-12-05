'''
Nicole Torres
CS2302: LAB6A
EXTRA CREDIT
12/04/18
'''
from collections import defaultdict


class Solution1:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        children = [set() for x in range(n)]
        for s, t in edges:
            children[s].add(t)
            children[t].add(s)
        leaves = [x for x in range(n) if len(children[x]) <= 1]
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for x in leaves:
                for y in children[x]:
                    children[y].remove(x)
                    if len(children[y]) == 1:
                        newLeaves.append(y)
            leaves = newLeaves
        return leaves


class Solution2:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = defaultdict(list)  # targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[:-1]:
            targets[a] += b,
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]


if __name__ == '__main__':

    # 1.
    listofedges = [[1, 0], [1, 2], [1, 3]]
    n = 4
    solu = Solution1()
    print()
    print('this is the solution to problem 1: ', solu.findMinHeightTrees(n, listofedges))
    print()

    # 2.
    airporttickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    solu2 = Solution2()
    print(solu2.findItinerary(airporttickets))

