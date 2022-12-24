class Queue:
  def __init__(self):
    self.data = []

  def size(self):
    return len(self.data)

  def enQueue(self, item):
    self.data.append(item)

  def deQueue(self):
    self.data.pop(0)

  def peek(self):
    return self.data[0]

  def isEmpty(self):
    return len(self.data) == 0

class SearchState:
  FIRST_MAX = 3
  SECOND_MAX = 4

  def __init__(self, f, s, p, h):
    self.first = f
    self.second = s
    self.parent = p
    self.howto = h
  
  def generate(self):
    # new generated states will be stored in the list below
    res = []
    # empty first
    if (self.first > 0):
      res.append(SearchState(0, self.second, self, "Empty First"))
    
    # empty second
    if (self.second > 0):
      res.append(SearchState(self.first, 0, self, "Empty Second"))
    
    # fill first
    if (self.first < SearchState.FIRST_MAX):
      res.append(SearchState(SearchState.FIRST_MAX, self.second, self, "Fill First"))
    
    # fill second
    if (self.second < SearchState.SECOND_MAX):
      res.append(SearchState(self.first, SearchState.SECOND_MAX, self, "Fill Second"))
    
    # pour first to second
    if (self.first > 0):
      if (self.first + self.second <= SearchState.SECOND_MAX):
        res.append(SearchState(0, self.first + self.second, self, "Pour First to Second"))
      else:
        res.append(SearchState(self.first + self.second - SearchState.SECOND_MAX, SearchState.SECOND_MAX, self, "Pour First to Second"))
    
    # pour second to first
    if (self.second > 0):
      if (self.first + self.second <= SearchState.FIRST_MAX):
        res.append(SearchState(self.first + self.second, 0, self, "Pour Second to First"))
      else:
        res.append(SearchState(SearchState.FIRST_MAX, self.first + self.second - SearchState.FIRST_MAX, self, "Pour Second to First"))

    return res

class WaterJugs:
  # Solving the water jug problem with BFS 
  def BFS(begin, target, firstMax, secondMax):
    queue = Queue()
    # initialization
    visited = [[False for c in range(secondMax+ 1)] for r in range(firstMax + 1)]
    # visited = []
    # for r in range(firstMax + 1):
    #   col = []
    #   for c in range(secondMax + 1):
    #     col.append(False)
    #   visited.append(col)
    SearchState.FIRST_MAX = firstMax
    SearchState.SECOND_MAX = secondMax
  
    queue.enQueue(begin)
    visited[begin.first][begin.second] = True
  
    while (not queue.isEmpty()):
      current = queue.peek()
      queue.deQueue()

      if (current.first == target or current.second == target):
        # construct the solution from current to the beginning  
        solution = ""
        while (current is not None):
          solution = ("%d %d - %s\n" % (current.first, current.second, current.howto)) + solution
          current = current.parent
        
        print(solution)
        return

      nextStates = current.generate()
      for i in range(len(nextStates)):
        if (visited[nextStates[i].first][nextStates[i].second]):
          continue

        queue.enQueue(nextStates[i])
        visited[nextStates[i].first][nextStates[i].second] = True

    print("No solution")


# client code
s = SearchState(0, 0, None, None)
WaterJugs.BFS(s, 45, 99, 100)
