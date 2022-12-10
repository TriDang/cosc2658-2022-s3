class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.balanced = True
  
  # calculate tree height
  # and check for balanced property at the same tiem
  def height(self):
    return self.heightRecursive()

  def isBalanced(self):
    self.height()  # just in case this method has not been called
    return self.balanced

  def heightRecursive(self):
    hl = hr = 0
    if self.left is not None:
      hl = self.left.heightRecursive()
    if self.right is not None:
      hr = self.right.heightRecursive()
    if (abs(hl - hr) > 1):
      self.balanced = False

    return 1 + max(hl, hr)

  # in-order traversal
  def inOrder(self):
    print("In-order traversal")
    self.inOrderRecursive()

  def inOrderRecursive(self):    
    # traverse left-subtree
    if self.left is not None:
      self.left.inOrderRecursive()

    # process root
    print(self.data)

    # traverse right-subtree
    if self.right is not None:
      self.right.inOrderRecursive()
  
  def __str__(self):
    return "Node data: " + str(self.data) + ", height: " + str(self.height()) + ", and balanced: " + str(self.balanced)

class Array2BalancedBST:
  def __init__(self, arr):
    self.arr = arr

  def build(self):
    return self.buildTree(self.arr, 0, len(self.arr) - 1)

  def buildTree(self, arr, left, right):
    if (left > right):
      return None

    mid = (left + right) // 2
    parent = TreeNode(arr[mid])
    parent.left = self.buildTree(arr, left, mid - 1)
    parent.right = self.buildTree(arr, mid + 1, right)
    return parent

class DataNode:
  def __init__(self, d):
    self.data = d
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def addToHead(self, newNode):
    if self.head is not None:
      newNode.next = self.head

    self.head = newNode

class List2BalancedBST:
  def __init__(self, lst):
    self.lst = lst

  def build(self):
    root = self.buildTree(self.lst.head, None)
    return root

  def buildTree(self, begin, end):
    if (begin == end):
      return None

    slow = begin
    fast = begin

    # when fast reaches the end, slow is in the middle
    while (fast is not end and fast.next is not end):
      fast = fast.next.next
      slow = slow.next

    parent = TreeNode(slow.data)
    parent.left = self.buildTree(begin, slow)
    parent.right = self.buildTree(slow.next, end)
    return parent

# root = Array2BalancedBST([1, 3, 5, 7, 9, 11, 20, 27, 33, 45, 60, 77, 82, 89, 99]).build()
# print(root)
# root.inOrder()

lst = LinkedList()
lst.addToHead(DataNode(99))
lst.addToHead(DataNode(95))
lst.addToHead(DataNode(89))
lst.addToHead(DataNode(72))
lst.addToHead(DataNode(67))
lst.addToHead(DataNode(53))
lst.addToHead(DataNode(22))
lst.addToHead(DataNode(19))
lst.addToHead(DataNode(13))
lst.addToHead(DataNode(11))
lst.addToHead(DataNode(7))
lst.addToHead(DataNode(3))
root2 = List2BalancedBST(lst).build()
print(root2)
root2.inOrder()