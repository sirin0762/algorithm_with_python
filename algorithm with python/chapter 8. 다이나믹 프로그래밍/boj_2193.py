# 이친수 : 1이 두번 연속 나오지 않는 이진수의 개수를 구해라

# 점화식을 알아보면 피보나치인 것을 알 수 있다.

n = int(input())

d = [0] * 100

def pibo(n):
  if n == 1 or n == 2:
    return 1

  return pibo(n-2) + pibo(n-1)

print(pibo(n))