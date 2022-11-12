class Node:
  def __init__(self, data = None):
    self.data = data
    self.next = None

class CList:
  def __init__(self):
    self.head = None
    self.size = 0

  def appendNode(self, newNode):
    if self.head is None:
      self.head = newNode
      newNode.next = self.head
      self.size = 1
      return

    # move to end of list
    temp = self.head
    i = 1
    while i < self.size:
      temp = temp.next
      i += 1
    temp.next = newNode
    newNode.next = self.head
    self.size += 1

  def removeNode(self, node):
    if self.size == 0:
      return
    if self.size == 1:
      if self.head == node:
        self.head = None
        self.size = 0
      else:
        return

    temp = self.head
    while temp.next != node:
      temp = temp.next
    if temp.next == self.head:
      self.head = self.head.next
    temp.next = temp.next.next
    self.size -= 1

# Test 1: n = 5, m = 2
print("Test 1: n = 5, m = 2")
n = 5
m = 2
list = CList()
for i in range(1, n + 1):
  list.appendNode(Node(i))

start = list.head
while list.size > 1:
  for i in range(m -1):
    start = start.next
  temp = start.next
  print("Remove", start.data)
  list.removeNode(start)
  start = temp

print("Remain", list.head.data)

# Test 2: n = 41, m = 3
print("Test 2: n = 41, m = 3")
n = 41
m = 3
list = CList()
for i in range(1, n + 1):
  list.appendNode(Node(i))

start = list.head
while list.size > 1:
  for i in range(m -1):
    start = start.next
  temp = start.next
  print("Remove", start.data)
  list.removeNode(start)
  start = temp

print("Remain", list.head.data)