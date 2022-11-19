class BSTNode:
  def __init__(self, data):
    self.data = data
    self.left = self.right = None

  def addChild(self, newNode):
    # add a new node as a new child of the current node
    # but if the current node has a child at the same location already
    # call this method recursively to the child
    if (newNode.data == self.data):
      # duplicated data => do nothing
      return

    if (newNode.data < self.data):
      if (self.left is None):
        self.left = newNode
      else:
        self.left.addChild(newNode)
    else:
      if (self.right is None):
        self.right = newNode
      else:
        self.right.addChild(newNode)

class BST:
  def __init__(self, data):
    self.root = BSTNode(data)

  def insert(self, newNode):
    self.root.addChild(newNode)

  def inOrder(self):
    # start the inOrder traversal from root
    self.inOrderRecursive(self.root)

  def visit(self, node):
    print(node.data)

  def inOrderRecursive(self, node):
    if (node is None):
      return
    # traverse left
    self.inOrderRecursive(node.left)
    # visit node
    self.visit(node)
    # traverse right
    self.inOrderRecursive(node.right)

  def search(self, x):
    # search for the value x in this tree
    # return the node containing x
    node = self.root
    comparison = 0
    while (node is not None):
      comparison += 1
      if (node.data == x):
        print("Number of comparisons to find", x, "is:", comparison)
        return node

      if (x < node.data):
        node = node.left
      else:
        node = node.right

    print("Cannot find", x, "after", comparison, "comparison(s)")


# 4, 2, 8, 3, 1, 7, 9, 6, 5
tree = BST(4)
tree.insert(BSTNode(2))
tree.insert(BSTNode(8))
tree.insert(BSTNode(3))
tree.insert(BSTNode(1))
tree.insert(BSTNode(7))
tree.insert(BSTNode(9))
tree.insert(BSTNode(6))
tree.insert(BSTNode(5))
# Let's traverse the tree using In-order
# the printed result must be an increasing list
tree.inOrder()
# Let's do some search
tree.search(4)
tree.search(3)
tree.search(5)
tree.search(10)
