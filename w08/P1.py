import time

MOD = 1000000007

def powerBruteForce(X, N):
  res = 1
  for i in range(N):
    res = (res * X) % MOD
  return res

def powerFast(X, N):
  if (N == 0):
    return 1

  if (N == 1):
      return X

  sub = powerFast(X, N // 2)
  sub = (sub * sub) % MOD
  if (N % 2 == 1):
    return (sub * X) % MOD

  return sub

# correctness test
print("Power brute force:", str(powerBruteForce(2, 100)))
print("Power decrease conquer:", str(powerFast(2, 100)))

print("Power brute force:", str(powerBruteForce(7, 10001)))
print("Power decrease conquer:", str(powerFast(7, 10001)))

# performance test
t1 = round(time.time_ns() / 1000000)
print("Power brute force:", str(powerBruteForce(201, 100000000)))
print("Brute force time: " + str(round(time.time_ns() / 1000000) - t1))

t1 = round(time.time_ns() / 1000000)
print("Power brute force:", str(powerFast(201, 100000000)))
print("Decrease conquer time: " + str(round(time.time_ns() / 1000000) - t1))
