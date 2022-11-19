class BinaryHeap:
  MAX_SIZE = 100

  def __init__(self):
    self.heap = [0] * BinaryHeap.MAX_SIZE
    self.size = 0

  def isEmpty(self):
    return (self.size == 0)

  # construct a heap from a list
  def buildHeap(self, arr):
    # first, copy the values from array to heap
    # and set the size accordingly
    self.size = len(arr)
    i = 0
    while (i < self.size):
      self.heap[i] = arr[i]
      i += 1

    # Note 1: we apply the heapify process to all internal nodes
    # because leaf nodes are heap already

    # Note 2: the number of internal nodes in a complete binary tree
    # of n nodes is floor(n/2)
    # https://en.wikipedia.org/wiki/Binary_tree#Properties_of_binary_trees

    i = self.size // 2
    while (i >= 0):
      self.heapify(i)
      i -= 1

  # heapify the tree whose root node has index nodeIdx
  # assumption: its two subtrees are heap already
  def heapify(self, nodeIdx):
    # index of left child 2 * nodeIdx + 1
    # index of right child 2 * nodeIdx + 2
    # index of parent (i - 1) // 2

    # if this node > left and right childdren => heap already
    # otherwise, exchange it with the max(left, right)
    maxIdx = nodeIdx
    # left child
    if (2 * nodeIdx + 1 < self.size and self.heap[2 * nodeIdx + 1] > self.heap[maxIdx]):
      maxIdx = 2 * nodeIdx + 1

    # right child
    if (2 * nodeIdx + 2 < self.size and self.heap[2 * nodeIdx + 2] > self.heap[maxIdx]):
      maxIdx = 2 * nodeIdx + 2

    # the element at nodeIdx is the maximum?
    if (maxIdx == nodeIdx):
      return

    # swap the element at nodeIdx with its maximum child
    self.heap[nodeIdx], self.heap[maxIdx] = self.heap[maxIdx], self.heap[nodeIdx]

    # recursively call heapify to the maximum child of nodeIdx
    self.heapify(maxIdx)

  def extractMax(self):
    # let's implement this method to extract the root of the heap
    # and use it to test the buildHeap method

    # first, save the value of root
    temp = self.heap[0]

    # now, copy the last node to root to maintain the SHAPE property
    self.heap[0] = self.heap[self.size - 1]

    # decrease the size
    self.size -= 1

    # make the remaining array a heap by calling heapify with the new root
    self.heapify(0)

    return temp

heap = BinaryHeap()
heap.buildHeap([5, 2, 8, 9, 3, 1, 4, 7, 6])
while (not heap.isEmpty()):
  print("Extract max:", heap.extractMax())
