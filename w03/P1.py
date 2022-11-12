class Node:
  def __init__(self, data = None):
    self.data = data
    self.next = None

# First, I will create a list like this
# n1 -> n2 -> n3 -> n4 -> n5 -> n2 (loop)
n1 = Node(1);
n2 = Node(2);
n3 = Node(3);
n4 = Node(4);
n5 = Node(5);

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n2

# Print the linked list
# add a counter to stop the loop

node = n1
stop = 0
print("Before loop removal")

while node is not None and stop < 10:
  print(node.data)
  node = node.next
  stop += 1

# when fast == slow: the 2 pointers pointed to
# one common node in the loop
loop = False  # if there is in fact a loop
fast = slow = n1
while True:
  if fast.next is None or fast.next.next is None:
    # those checks ensure that nothing happen if there is in fact NO loop
    break
  fast = fast.next.next
  slow = slow.next
  if fast == slow:
    loop = True
    break

# now, stop fast, advance slow to count how many nodes in the loop
if loop:
  nodesInLoop = 1
  while slow.next != fast:
    slow = slow.next
    nodesInLoop += 1

# now, position fast <nodesInLoop> positions before slow
# and advance them at the same speed
# their will meet at the first intersected node
fast = slow = n1
for i in range(nodesInLoop):
  fast = fast.next

while slow.next != fast.next:
  slow = slow.next
  fast = fast.next

# remove the loop
fast.next = None

# traverse and display the linked list again
node = n1
stop = 0
print("After loop removal")
while node is not None and stop < 10:
  print(node.data)
  node = node.next
  stop += 1
