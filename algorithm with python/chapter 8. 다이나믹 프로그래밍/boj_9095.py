# 9095번
# 주어진 정수를 1, 2, 3의 숫자를 더함으로써 만드는 경우의 수를 구하시오.

n = int(input())

d = [0] * 100
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, n + 1):
  d[i] = d[i - 1] + d[i - 2] + d[i - 3]

print(d[n])

