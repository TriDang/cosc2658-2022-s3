# Lomuto partition
# Return a partition point p
# Where all elements arr[left, p - 1] <= arr[p] <= all elements arr[p + 1, right]
def partitionL(arr, left, right):
  p = arr[right]  # select the right-most element as pivot
  i = left
  for j in range(left, right):
    if (arr[j] <= p):
      # swap      
      arr[i], arr[j] = arr[j], arr[i]

      # increase i
      i += 1
      
  # swap => position pivot to the correct location
  arr[i], arr[right] = arr[right], arr[i]
  return i

# Hoare partition
# Return a partition point p
# Where all elements arr[left, p] <= all elements arr[p + 1, right]
def partitionH(arr, left, right):
  p = arr[left]  # select the left-most element as pivot
  front = left
  back = right
  while (True):
    while (arr[front] < p):
      front += 1
    while (arr[back] > p):
      back -= 1
    if (front >= back):
      return back
    
    # swap
    arr[front], arr[back] = arr[back], arr[front]
    front += 1
    back -= 1

# quick select - Lomuto partition
def quickSelectL(arr, left, right, k):
  p = partitionL(arr, left, right)
  if (k - 1 == p):
    return arr[p]

  if (k - 1 > p):
    return quickSelectL(arr, p + 1, right, k)

  return quickSelectL(arr, left, p - 1, k)

# quick select - Hoare partition
def quickSelectH(arr, left, right, k):
  if (left == right):
    return arr[left]

  p = partitionH(arr, left, right)
  if (k - 1 <= p):
    return quickSelectH(arr, left, p, k)

  return quickSelectH(arr, p + 1, right, k)

# Lomuto partition
test = [3, 5, 2, 1, 8, 9, 6, 7, 4]
smallest = quickSelectL(test, 0, len(test) - 1, 1)
print("Smallest:", smallest)

test = [3, 5, 2, 1, 8, 9, 6, 7, 4]
secondSmallest = quickSelectL(test, 0, len(test) - 1, 2)
print("Second smallest:", secondSmallest)

test = [3, 5, 2, 1, 8, 9, 6, 7, 4]
fifthSmallest = quickSelectL(test, 0, len(test) - 1, 5)
print("Fifth smallest:", fifthSmallest)

# Hoare partition
test = [3, 5, 2, 1, 8, 9, 6, 7, 4]
smallest = quickSelectH(test, 0, len(test) - 1, 1)
print("Smallest:", smallest)

test = [3, 5, 2, 1, 8, 9, 6, 7, 4]
secondSmallest = quickSelectH(test, 0, len(test) - 1, 2)
print("Second smallest:", secondSmallest)

test = [3, 5, 2, 1, 8, 9, 6, 7, 4]
fifthSmallest = quickSelectH(test, 0, len(test) - 1, 5)
print("Fifth smallest:", fifthSmallest)
