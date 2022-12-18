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

class Course:
  def __init__(self, n, i):
    self.name = n
    self.index = i
    self.inDegree = 0
    self.visited = False

  def increaseDegree(self):
    self.inDegree += 1

  def decreaseDegree(self):
    self.inDegree -= 1

  def isSource(self):
    return (self.inDegree == 0)

def topoSort(courseNames, requires):
  # initialization
  n = len(courseNames)
  res = []
  courses = []
  queue = Queue()

  # course objects creation
  for i in range(n):
    courses.append(Course(courseNames[i], i))
    # indegree calculation
    for j in range(n):
      if (requires[i][j] != 0):
        courses[i].increaseDegree()

  # enqueue the source vertices
  for i in range(n):
    if (courses[i].isSource()):
      queue.enQueue(courses[i])
      courses[i].visited = True

  while (not queue.isEmpty()):
    u = queue.peek()
    queue.deQueue()
    res.append(u.name)

    source = u.index
    for target in range(n):
      if (requires[target][source] != 0):
        if (not courses[target].visited):
          courses[target].decreaseDegree()
          if (courses[target].isSource()):
            queue.enQueue(courses[target])
            courses[target].visited = True
  return res


courses = [
  "Intro to Programming",
  "Programming 1",
  "Algorithms",
  "Database Applications"
]

requires = [
  [0, 0, 0, 0],
  [1, 0, 0, 0],
  [1, 0, 0, 1],
  [1, 0, 1, 0]
]

learningOrder = topoSort(courses, requires)
if (len(learningOrder) < len(courses)):
  print("Cannot take all courses")
print(learningOrder)
