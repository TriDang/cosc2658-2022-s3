import random
import time

def coutnInversionBruteforce(arr):
  res = 0
  for i in range(len(arr)):
    for j in range(i  + 1, len(arr)):
      if (arr[i] > arr[j]):
        res += 1
  return res

def countInversionDivideConquer(arr):
  res = 0
  if (len(arr) == 1):
    return res

  mid = len(arr) // 2
  left = [0] * mid
  right = [0] * (len(arr) - mid)

  for i in range(mid):
    left[i] = arr[i]

  for i in range(mid, len(arr)):
    right[i - mid] = arr[i]

  res = countInversionDivideConquer(left) + countInversionDivideConquer(right)
  
  res += merge(left, right, arr)
  
  return res

def merge(left, right, dest):
  res = 0
  pLeft = 0
  pRight = 0
  pDest = 0
  while (pLeft < len(left) and pRight < len(right)):
    if (left[pLeft] <= right[pRight]):
      dest[pDest] = left[pLeft]
      pDest += 1
      pLeft += 1
    else:
      dest[pDest] = right[pRight]
      pDest += 1
      pRight +=1
      res += (len(left) - pLeft)

  while pLeft < len(left):
    dest[pDest] = left[pLeft]
    pDest += 1
    pLeft += 1

  while pRight < len(right):
    dest[pDest] = right[pRight]
    pDest += 1
    pRight += 1

  return res

test1 = [1, 2, 3, 4, 5, 6, 7, 8]
# inversion = 0
print(coutnInversionBruteforce(test1))
print(countInversionDivideConquer(test1))

test2 = [1, 2, 3, 4, 5, 6, 8, 7]
# inversion = 1
print(coutnInversionBruteforce(test2))
print(countInversionDivideConquer(test2))

test3 = [5, 4, 3, 2, 1]
# inversion = 10
print(coutnInversionBruteforce(test3))
print(countInversionDivideConquer(test3))

# correctness test
SIZE = 2000
test4 = [0] * SIZE
for i in range(SIZE):
  test4[i] = random.randint(1, SIZE)

print(coutnInversionBruteforce(test4))
print(countInversionDivideConquer(test4))

# performance test
SIZE = 20000
test5 = [0] * SIZE
for i in range(SIZE):
  test5[i] = random.randint(1, SIZE)
t1 = round(time.time_ns() / 1000000)  # nano to milli
print(coutnInversionBruteforce(test5))
print("Brute force time: " + str(round(time.time_ns() / 1000000) - t1))

t1 = round(time.time_ns() / 1000000)  # nano to milli
print(countInversionDivideConquer(test5))
print("Divide and Conquer time: " + str(round(time.time_ns() / 1000000) - t1))