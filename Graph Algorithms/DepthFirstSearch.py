'''
Author : Karthik Goudar
Date   : 3 Feb, 2023


Depth First Search Algorithm

Depth-First Search (DFS) is an algorithm for traversing or searching a tree or graph data structure.
It starts at the tree root (or some arbitrary node of a graph) and explores as far as possible along each branch before backtracking.


DFS algorithm starts at node 0 and explores as far as possible along each branch before backtracking.
 The algorithm continues this process until it has traversed all the nodes in the graph.


'''



from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS(i, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

visited = [False] * (len(g.graph))
g.DFS(2, visited)
