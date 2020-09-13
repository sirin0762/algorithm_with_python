# 인접하지 않은 식량 창고를 털어라

n = int(input())

k = list(map(int, input().split()))

d = [0] * 100

d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, k):
    d[i] = max(d[i - 1], d[i - 2] + k[i])

print(d[n - 1])