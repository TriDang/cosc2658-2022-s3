# we can use DFS or BFS to solve this problem
# start from any node, assign either D (data structures) or A (algorithms) to it
# then, assign a different value to all its neighbors
# but, if a neighbor has a value already and that value conflicts
# with this current node => no solution

# this kind of graph is called Bipartite graph
# https://en.wikipedia.org/wiki/Bipartite_graph

def DFS(matrix, current, visited, values):
  # get all neighbors
  n = len(visited)
  res = True
  for i in range(n):
    if (matrix[current][i] != 0):
      if (not visited[i]):
        if (values[current] == 'A'):
          values[i] = 'D'
        else:
          values[i] = 'A'
        visited[i] = True
        res = res and DFS(matrix, i, visited, values)
      else:
        if (values[i] == values[current]):
          return False
  return res

def isBipartite(matrix):
  n = len(matrix)
  visited = [False] * n
  values = [' '] * n
  res = True
  for i in range(n):
    if (not visited[i]):
      values[i] = 'A'
      visited[i] = True
      res = res and DFS(matrix, i, visited, values)
  return res

# client code
# one is friend with two others => true
print(isBipartite([
  [0, 1, 1],
  [1, 0, 0],
  [1, 0, 0]
]))

# no one is friend with other => true
print(isBipartite([
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]))

# there is a friendship between any pair => false
print(isBipartite([
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0]
]))

# all odd indices are in one group, all even indices are in another group => true
print(isBipartite([
  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
]))

# similar to the previous case, but the two even last people
# are friend => cannot divide => false
print(isBipartite([
  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],  # there is a change
  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 1, 1, 0]   # there is a change
]))
