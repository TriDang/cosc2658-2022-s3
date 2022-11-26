import time
import random

# generate a list of random integer
def create_list(arr_size, arr_range):
  res = [random.randint(1, arr_range) for i in range(arr_size)]
  return res

# counting sort
# assumption: elements are in the range[1, arr_range]
def counting_sort(arr, arr_range):
  freq = [0] * (arr_range + 1)  # frequency array
  res = [0] * len(arr)  # result array

  # freq counting
  for i in range(len(arr)):
    freq[arr[i]] += 1

  # calculate cumulative freq
  for i in range(1, arr_range + 1):
    freq[i] += freq[i-1]

  # distribution step (right to left to make the sort stable)
  for i in range(len(arr)-1, -1, -1):
    res[freq[arr[i]]-1] = arr[i]
    freq[arr[i]] -= 1

  return res

# Correctness test
test1 = create_list(10, 10)
print("Before sort")
print(test1)
print("After sort")
print(counting_sort(test1, 10))

# Performance test
test2 = create_list(1000000, 1000)
t1 = round(time.time_ns() / 1000000)  # nano to milli
counting_sort(test2, 1000)
t2 = round(time.time_ns() / 1000000)
print("Counting sort time:", t2 - t1, "milliseconds")

t3 = round(time.time_ns() / 1000000)
sorted(test2)
t4 = round(time.time_ns() / 1000000)
print("Python sort time:", t4 - t3, "milliseconds")
