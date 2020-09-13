# 2xn 타일링

w = int(input())

d = [0] * (w + 1)

d[1] = 1
d[2] = 2

for i in range(3, w + 1):
  d[i] = (d[i - 1] + d[i - 2]) % 10007

print(d[w])