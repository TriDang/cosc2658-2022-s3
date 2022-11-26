class RMITStudent:
  def __init__(self, id, name, m, mark):
    self.studentId = id
    self.fullName = name
    self.major = m
    self.GPA = mark

  def __str__(self):
    return "Id: " + self.studentId + \
           ", Fullname: " + self.fullName + \
           ", Major: " + self.major + \
           ", GPA: " + str(self.GPA)

class RMITStudentNode:
  def __init__(self, student):
    self.data = student
    self.next = None

class RMITStudentList:
  def __init__(self):
    self.head = None
    self.size = 0

  # insert a student node at the end
  # because we have to check for duplicated student Id
  def insert(self, newStudent):
    if (self.size == 0):
      self.head = RMITStudentNode(newStudent)
      self.size = 1
      return True

    parent = None
    current = self.head
    while (current is not None):
      if (current.data.studentId == newStudent.studentId):
        # duplicated id
        return False
      # advance pointers
      parent = current
      current = current.next
    parent.next = RMITStudentNode(newStudent)
    self.size += 1
    return True

  # return a student with the provided id
  # or None if there is no such student
  def get(self, studentId):
    node = self.head
    while (node is not None):
      if (node.data.studentId == studentId):
        return node.data
      node = node.next

    # no matching node
    return None

  # remove a student with a provided student id
  # return true or false if the remove is successful or not
  def remove(self, studentId):
    if (self.size == 0):
      return False

    parent = None
    current = self.head
    while (current is not None):
      if (current.data.studentId == studentId):
        if (current == self.head):
          # remove head => need to update head
          self.head = self.head.next
          self.size -= 1
          return True

        parent.next = current.next
        size -= 1
        return True

      #advance
      parent = current
      current = current.next

    # No matching node
    return False

class RMITStudentCollectionChaining:
  def __init__(self, tableSize):
    self.N = tableSize
    self.hashTable = [None] * tableSize

  def hashCharacter(self, c):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".index(c)

  def hashString(self, s):
    res = 0
    for c in s:
      res += self.hashCharacter(c)

    return res % self.N

  def put(self, newStudent):
    hash = self.hashString(newStudent.studentId)
    # no list at this location?
    if (self.hashTable[hash] is None):
      self.hashTable[hash] = RMITStudentList()

    return self.hashTable[hash].insert(newStudent)

  def get(self, studentId):
    hash = self.hashString(studentId)
    if (self.hashTable[hash] is None):
      return None
    return self.hashTable[hash].get(studentId)

  def remove(self, studentId):
    hash = self.hashString(studentId)
    if (self.hashTable[hash] is None):
      return False
    return self.hashTable[hash].remove(studentId)

# client code
collection = RMITStudentCollectionChaining(13)

# all student records have the same hash value
# and will be in the same list
collection.put(RMITStudent("S123", "Alice", "IT", 3.6))
collection.put(RMITStudent("S321", "Bob", "SE", 4.0))
collection.put(RMITStudent("S231", "Carol", "CS", 3.8))
print(collection.get("S123"))  # Alice
print(collection.get("S231"))  # Carol
print(collection.get("S213"))  # None

# Verify if 12 out of 13 slots in the hash table are None
nullCount = 0
for i in range(13):
  if (collection.hashTable[i] is None):
    nullCount += 1
print("Null count:", nullCount)  # must be 12

# add another student, this time let's try a different hash
collection.put(RMITStudent("S124", "Dang", "IS", 3.5))

# Verify if 11 out of 13 slots in the hash table are None
nullCount = 0
for i in range(13):
  if (collection.hashTable[i] is None):
    nullCount += 1
print("Null count:", nullCount)  # must be 11

# let's remove one of the student and try to get that student again
collection.remove("S123")
# let access that student again, must be None now
print(collection.get("S123"))  # None
