class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = self.right = None

  def height(self):
    # the height of a node = max(left.height, right.height) + 1
    maxHeight = 0
    if (self.left is not None):
      maxHeight = max(maxHeight, self.left.height())
    if (self.right is not None):
      maxHeight = max(maxHeight, self.right.height())
    return maxHeight + 1

# let's create this tree
# root contains [child1, child2]
# child1 contains [child11]
# child11 contains [child111] 
# height => 4

root = TreeNode("root")
# At this time, the height of the tree whose root is "root" = 1
print("Tree height:", root.height())
    
child1 = TreeNode("child 1")
child2 = TreeNode("child 2")
root.left = child1
root.right = child2
# At this time, the height of the tree whose root is "root" = 2
print("Tree height:", root.height())
child11 = TreeNode("child 11")
child111 = TreeNode("child 111")
child1.left = child11
child11.left = child111
# At this time, the height of the tree whose root is "root" = 4
print("Tree height:", root.height())
