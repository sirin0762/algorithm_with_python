data = list(map(int, input()))

answer = 1

for i in data:
  if i:
    answer *= i

print(answer + data.count(1))
