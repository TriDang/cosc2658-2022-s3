def longestIncreasingSubsequence(arr):
  n = len(arr)

  maxCount = [1] * n
  # maxCount[i] stores the length of the longest increasing subsequence ending at i
  # maxCount[i] must be at least 1 (the subsequence contains only element i)

  prevElement = [0] * n
  # prevElement[i] stores the index of the previous element of the
  # longest increasing subsequence that ends at element i
  # use this array to trace back to the first element
  for i in range(n):
    prevElement[i] = -1

  # calculate the longest increasing subsequence for all ending elements
  for i in range(n):
    for j in range(i):
      if (arr[i] > arr[j]):
        # we can expand the subsequence ends at j-th
        # to include the element i-th?
        if (maxCount[i] < maxCount[j] + 1):
          maxCount[i] = maxCount[j] + 1
          prevElement[i] = j

  # get the longest subsequence
  # the longest subsequence has to end at one of the element 0 -> (n-1)
  maxEnding = 0
  for i in range(n):
    if (maxCount[maxEnding] < maxCount[i]):
      maxEnding = i

  # Go backward from maxEnding index to the first element
  # to construct the solution
  elements = []
  while (maxEnding != -1):
    # in this implementation, the values of the elements in the
    # longest increasing subsequence are returned
    # you can change the assignment below to return the indices
    # of the elements instead, i.e., elements.push(maxEnding)
    elements.insert(0, arr[maxEnding])
    maxEnding = prevElement[maxEnding]

  # display result
  print("Length of the longest increasing subsequence", len(elements))
  print("The elements are: ")
  for e in elements:
    print(e, " ", end="")

test = [5, 2, 3, 9, 6, 7, 8, 1]
longestIncreasingSubsequence(test)
