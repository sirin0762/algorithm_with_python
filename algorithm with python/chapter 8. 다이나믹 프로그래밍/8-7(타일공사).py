# 바닥에 타일을 까는데 가능한 경우의 수

n = int(input())

d = [0] * 100

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

print(d[n])