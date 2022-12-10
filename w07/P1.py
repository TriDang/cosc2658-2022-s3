import time
import random

def generate(size, value_range):
  res = [random.randint(1, value_range) for i in range(size)]
  return res

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

# sort with quick sort
# Lomuto partition method
def quickSortL(arr, left, right):
  if (left < right):
    p = partitionL(arr, left, right)
    quickSortL(arr, left, p - 1)
    quickSortL(arr, p + 1, right)

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

# sort with quick sort
# using the Hoare partition method
def quickSortH(arr, left, right):
  if (left < right):
    p = partitionH(arr, left, right)
    quickSortH(arr, left, p)
    quickSortH(arr, p + 1, right)

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

# Correctness test
arr1 = generate(10, 10)
print("Before merge sort")
print(arr1)
mergeSort(arr1)
print("After merge sort")
print(arr1)

arr2 = generate(10, 10)
print("Before quick sort/Lomuto partition")
print(arr2)
quickSortL(arr2, 0, len(arr2) - 1)
print("After quick sort/Lomuto partition")
print(arr2)

arr3 = generate(10, 10)
print("Before quick sort/Hoare partition")
print(arr3)
quickSortL(arr3, 0, len(arr3) - 1)
print("After quick sort/Hoare partition")
print(arr3)


# Performance test
arr4 = generate(100000, 10000)
t1 = round(time.time_ns() / 1000000)  # nano to milli
mergeSort(arr4)
t2 = round(time.time_ns() / 1000000)
print("Merge sort time (ms):", (t2 - t1))

arr5 = generate(100000, 10000)
t1 = round(time.time_ns() / 1000000)  # nano to milli
quickSortL(arr5, 0, len(arr5) - 1)
t2 = round(time.time_ns() / 1000000)
print("Quick sort/Lomuto partition time (ms):", (t2 - t1))

arr6 = generate(100000, 10000)
t1 = round(time.time_ns() / 1000000)  # nano to milli
quickSortH(arr6, 0, len(arr6) - 1)
t2 = round(time.time_ns() / 1000000)
print("Quick sort/Hoare partition time (ms):", (t2 - t1))