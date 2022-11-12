class Stack:
  def __init__(self):
    self.elements = []

  def push(self, ele):
    self.elements.append(ele)
  
  def pop(self):
    self.elements.pop()
  
  def peek(self):
    return self.elements[-1]

  def isEmpty(self):
    return len(self.elements) == 0

def isBalance(s):
  st = Stack()
  for c in s:
    if c == "[" or c == "{" or c == "(":
      st.push(c)
      continue
    if st.isEmpty():
      return False
    c2 = st.peek()
    st.pop()
    if (c == ']' and c2 != '[') or \
       (c == ')' and c2 != '(') or \
       (c == '}' and c2 != '{'):
      return False
  if st.isEmpty():
    return True
  return False

print("[]:", isBalance("[]"))  # True
print("[](){}:", isBalance("[](){}"))  # True
print("{[]}(()):", isBalance("{[]}(())"));  # True
print("][)(}{:", isBalance("][)(}{"));  # False
print("(((((((((()))))))))}:", isBalance("(((((((((()))))))))}"));  # False