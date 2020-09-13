# 연속 3잔의 포도주를 마시는 것은 불가능
# 포도주의 최대값
# 2579(계단오르기)와 같은 알고리즘

n = int(input())

wines = [int(input()) for _ in range(n)]

d = [0] * n

d[0] = wines[0]
d[1] = d[0] + wines[1]

for i in range(3, n):
  d[i] = max(d[i - 2] + wines[i], d[i - 3] + wines[i - 1] + wines[i], d[i - 1])

print(d[n - 1])
