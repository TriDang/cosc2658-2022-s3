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

class RMITStudentCollectionLinearProbing:
  DELETED = RMITStudent("S000", "DELETED", "NONE", 0.0)

  def __init__(self, tableSize):
    self.N = tableSize
    self.size = 0
    self.hashTable = [None] * tableSize

  def hashCharacter(self, c):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".index(c)

  def hashString(self, s):
    res = 0
    for c in s:
      res += self.hashCharacter(c)

    return res % self.N

  def put(self, newStudent):
    if (self.size == self.N):
      return False
    hash = self.hashString(newStudent.studentId)

    while (self.hashTable[hash] is not None and self.hashTable[hash] is not self.DELETED):
      # the calculated position has been occupied (collision)
      # check if there is a duplicated id
      if (self.hashTable[hash].studentId == newStudent.studentId):
        return False

      # try the next position
      # make sure hash is not out of range
      hash = (hash + 1) % self.N

    self.hashTable[hash] = newStudent
    self.size += 1
    return True

  def get(self, studentId):
    hash = self.hashString(studentId)
    while (self.hashTable[hash] is not None):
      # is this the correct student?
      if (self.hashTable[hash].studentId == studentId):
        return self.hashTable[hash]

      # try the next position
      hash = (hash + 1) % self.N

    return None

  def remove(self, studentId):
    hash = self.hashString(studentId)
    while (self.hashTable[hash] is not None):
      # is this the correct student?
      if (self.hashTable[hash].studentId == studentId):
        self.hashTable[hash] = self.DELETED
        self.size -= 1
        return True

      # try the next position
      hash = (hash + 1) % self.N

    return False

# client code
collection = RMITStudentCollectionLinearProbing(13)

# Alice -> Bob -> Carol
collection.put(RMITStudent("S123", "Alice", "IT", 3.6))
collection.put(RMITStudent("S321", "Bob", "SE", 4.0))
collection.put(RMITStudent("S231", "Carol", "CS", 3.8))
print(collection.get("S123"))  # Alice
print(collection.get("S231"))  # Carol

# Remove Bob - the middle element
collection.remove("S321")
# Check if Bob has been replaced by DELETED
print(collection.hashTable[(collection.hashString("S321") + 1) % collection.N])
# Try to access Carol again
print(collection.get("S231"))  # Carol
# Add a new student having the same hash value
collection.put(RMITStudent("S312", "Dang", "IS", 3.5))
# Check if the new student occupies the slot of Bob before
print(collection.hashTable[(collection.hashString("S321") + 1) % collection.N])
