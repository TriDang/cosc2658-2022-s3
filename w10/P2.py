def minimumSpanningTree(nodes):
  INFINITY = 999999
  n = len(nodes)
  length = 0

  # use this array to mark nodes have been added already
  added = [False] * n

  # distance between the tree being built and not-yet-added nodes
  distances = [INFINITY] * n
  # insert node zero (any node is OK) first, so set its distance to zero
  distances[0] = 0
  
  # stop when the number of added nodes = n
  nodeCount = 0
  while (nodeCount < n):
    shortest = INFINITY
    shortestNode = -1  # index of the node having the shortest distance to the tree

    # determine the shortest distance node to the tree
    for i in range(n):
      if (added[i]):
        continue

      if (shortest > distances[i]):
        shortest = distances[i]
        shortestNode = i

    if (shortest == INFINITY):
      # we cannot go further - the graph is not connected
      return INFINITY

    # add the shortest node to the tree
    added[shortestNode] = True
    length += distances[shortestNode]
    nodeCount += 1

    # update other distances to the tree
    for i in range(n):
      if (added[i]):
        continue

      if (nodes[shortestNode][i] > 0):  # shortestNode and i are connected
        if (distances[i] > nodes[shortestNode][i]):  # whether connect through shortestNode is better?
          distances[i] = nodes[shortestNode][i]

  return length;

castles = [
  [0, 1, 9, 8],
  [1, 0, 3, 5],
  [9, 3, 0, 4],
  [8, 5, 4, 0]
]
print("Shortest total length:", minimumSpanningTree(castles))
