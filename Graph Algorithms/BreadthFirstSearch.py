'''
Author : Karthik Goudar
Date   : 2 Feb, 2023


Breadth First Search Algorithm

Breadth-First Search (BFS) is an algorithm for traversing or searching a tree or graph data structure.
 It starts at the tree root (or some arbitrary node of a graph) and explores the neighbor nodes first,
  before moving to the next level neighbors.

BFS algorithm starts at node 0 and explores all the neighbor nodes at the current depth level before moving on to the next level.
The algorithm continues this process until it has traversed all the nodes in the graph.

'''



from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)
