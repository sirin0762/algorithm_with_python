# 피보나치 수열에서 pibo(0), pibo(1)이 몇 번 호출 되는가

w = int(input())

zero, one = 0, 0

def pibo(n):
  global zero, one
  if n == 0:
    zero += 1
    return 0
  
  if n == 1:
    one += 1
    return 1
  
  return pibo(n - 1) + pibo(n - 2)

pibo(w)

print(zero, one)