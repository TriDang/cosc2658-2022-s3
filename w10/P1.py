def shortestPath(nodes, src, dest):
  INFINITY = 999999
  n = len(nodes)
  
  distances = [INFINITY] * n  # distance[i] stores the minimum distance from src to i
  visited = [False] * n  # visited state
  previous = [-1] * n  # used to construct the shortest path

  distances[src] = 0  # zero distance from the src to itself
  visited[src] = True

  current = src
  while (True):
    # update the shortest distance through current node to all un-visited nodes
    for i in range(n):
      if (visited[i]):
        continue

      if (nodes[current][i] > 0):  # current and i are connected?
        # distance to i > distance reached through "current"
        if (distances[i] > distances[current] + nodes[current][i]):
          distances[i] = distances[current] + nodes[current][i]
          previous[i] = current

    # use the shortest distance node as the new current
    shortest = INFINITY
    for i in range(n):
      if (visited[i]):
        continue

      if (shortest > distances[i]):
        shortest = distances[i]
        current = i

    if (current == dest):
      # we reach the destination
      # display the shortest path
      path = str(current) + " "
      while (current != src):
        current = previous[current]
        path = str(current) + " -> " + path

      print("Shortest path:", path)
      return distances[dest]

    if (shortest == INFINITY):
      # we cannot go further
      return INFINITY

    # continue the next round
    visited[current] = True

distances = [
  [0, 3, 2, 0],
  [3, 0, 0, 0],
  [2, 0, 0, 0],
  [0, 0, 0, 0]
]
print("Shortest distance:", shortestPath(distances, 0, len(distances) - 1))
