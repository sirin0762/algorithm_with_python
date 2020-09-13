# 분명 다이나믹 분류에 들어가 있는데.. 그리디로 품..

# 2839번

n = int(input())
answer = -1

for i in range((n // 3)+1):
  if (n - (i * 3)) % 5 == 0:
    answer = i + ((n - (i * 3)) // 5)
    break

print(answer)

# 추가. 다이나믹으로

w = int(input())

kilos = [3, 5]

d = [1000] * (w + 1)

d[0] = 0

for i in range(len(kilos)):
  for j in range(kilos[i], w + 1):
    if d[j - kilos[i]] != 1000:
      d[j] = min(d[j], d[j - kilos[i]] + 1)

if d[w] != 1000:
  print(d[w])
else:
  print('-1')