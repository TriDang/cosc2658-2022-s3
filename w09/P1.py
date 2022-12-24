import random

def equalCandiesBruteForce(boxes):
  res = 999999999
  for i in range(len(boxes)):
    tot = 0
    for j in range(len(boxes)):
      tot += abs(boxes[j] - boxes[i])

    if (tot < res):
      res = tot

  return res

def equalCandiesTransform(boxes):
  mergeSort(boxes)

  # pick the median
  med = boxes[len(boxes) // 2]
  res = 0
  for i in range(len(boxes)):
    res += abs(boxes[i] - med)

  return res

# reuse Merge Sort code in week 7
def mergeSort(arr):
  if len(arr) > 1:
    n = len(arr)
    middle = n // 2

    # create 2 sub-arrays from arr
    sub1 = [0] * middle
    for i in range(middle):
      sub1[i] = arr[i]

    sub2 = [0] * (n - middle)
    for i in range(middle, n):
      sub2[i - middle] = arr[i]

    # sort first and second halves
    mergeSort(sub1)
    mergeSort(sub2)

    # merge sub1 and sub2 into the original array
    merge(sub1, sub2, arr)

# merge two sub-arrays sub1 and sub2 into the array dest
def merge(sub1, sub2, dest):
  # pointers to 3 arrays
  p1 = 0
  p2 = 0
  pDest = 0

  while (p1 < len(sub1) and p2 < len(sub2)):
    if (sub1[p1] <= sub2[p2]):
      dest[pDest] = sub1[p1]
      p1 += 1
    else:
      dest[pDest] = sub2[p2]
      p2 += 1
    pDest += 1

  # copy remaining elements, if any
  while (p1 < len(sub1)):
    dest[pDest] = sub1[p1]
    pDest += 1
    p1 += 1

  while (p2 < len(sub2)):
    dest[pDest] = sub2[p2]
    pDest += 1
    p2 += 1

# client code
print(equalCandiesBruteForce([5, 8, 3]))
print(equalCandiesTransform([5, 8, 3]))

print(equalCandiesBruteForce([9, 9, 9, 9, 9, 10]))
print(equalCandiesTransform([9, 9, 9, 9, 9, 10]))

SIZE = 1000
test = [0] * SIZE
for i in range(SIZE):
  test[i] = random.randint(1, SIZE)
print(equalCandiesBruteForce(test.copy()))
print(equalCandiesTransform(test))

