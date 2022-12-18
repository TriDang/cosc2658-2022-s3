import math

def sqrt(X):
  eps = 0.0000001
  min = 0
  max = X
  if (X < 1):
    max = 1

  while (max - min > eps):
    mid = (min + max) / 2.0
    if (mid * mid < X):
      min = mid
    else:
      max = mid
  return max

print("Built-in sqrt(5): %.6f" % math.sqrt(5))
print("Binary search sqrt(5): %.6f" % sqrt(5))

print("Built-in sqrt(101): %.6f" % math.sqrt(101))
print("Binary search sqrt(101): %.6f" % sqrt(101))

print("Built-in sqrt(0.5): %.6f" % math.sqrt(0.5))
print("Binary search sqrt(0.5): %.6f" % sqrt(0.5))