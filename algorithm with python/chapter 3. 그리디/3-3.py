# 숫자 카드 게임
n, m = map(int, input().split())
result = []

for _ in range(n):
  result.append(min(list(map(int, input().split()))))

print(max(result))
