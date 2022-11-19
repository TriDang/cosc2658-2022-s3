class Graph:
  # create a graph with the number of nodes/vertices
  def __init__(self, nodes):
    self.size = nodes
    self.matrix = [[0 for i in range(self.size)] for j in range(self.size)]
    self.nodeLabels = [""] * self.size

  # set the label for a node
  def setNodeLabel(self, nodeIdx, label):
    self.nodeLabels[nodeIdx] = label

  # create an edge between two nodes
  def addEdge(self, node1, node2):
    self.matrix[node1][node2] = 1
    # for undirected graph, node1 -> node2 also means node2 -> node1
    self.matrix[node2][node1] = 1

  # depth-first search/traversal
  def DFS(self):
    print("Depth-First Search/Traversal")
    # visited states
    visited = [False] * self.size
    # start the DFS recursively from node 0 (you can start from any node)
    self.DFSR(0, visited)

    # the above code assumes the graph is connected
    # that mean you can reach all nodes from any node
    # if the graph is not connected, you must call DFSR on every node
    # to make sure you visit all nodes (lecture 4, slide 68)

  def DFSR(self, nodeIdx, visited):
    if (visited[nodeIdx]):
      # this node has been visited before
      return

    # this is the "visit" operation
    # do whatever you want with this node
    print("Visit:", self.nodeLabels[nodeIdx])
    # mark the visited state
    visited[nodeIdx] = True
    # apply the DFS process to all adjacent nodes
    i = 0
    while (i < self.size):
      if (self.matrix[nodeIdx][i] == 1 and (not visited[i])):
        self.DFSR(i, visited)
      i += 1

  # breadth-first search/traversal
  def BFS(self):
    print("Breadth-First Search/Traversal")
    # visited states
    visited = [False] * self.size

    # use a queue to implement BFS
    # we can use the built-in list ADT
    queue = []
    
    # start from node 0 (any node is OK)
    queue.append(0)
    visited[0] = True

    while (len(queue) > 0):
      nodeIdx = queue.pop(0)
      # "visit" this node
      print("Visit:", self.nodeLabels[nodeIdx])

      # add all adjacent nodes to the queue
      for i in range(self.size):
        if (self.matrix[nodeIdx][i] == 1 and (not visited[i])):
          queue.append(i)
          visited[i] = True

g = Graph(6)
g.setNodeLabel(0, "A")
g.setNodeLabel(1, "B")
g.setNodeLabel(2, "C")
g.setNodeLabel(3, "D")
g.setNodeLabel(4, "E")
g.setNodeLabel(5, "F")
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 0)
g.addEdge(1, 4)
g.DFS()
g.BFS()
