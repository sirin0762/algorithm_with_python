# 데이터 정렬이 안되있음 -> no binary
# 순차 탐색으로
# 수열의 부분 합

n, s = map(int, input().split())

list_n = list(map(int, input().split()))

min_length = len(list_n)

for i in range(n):
  for j in range(i + 1, n):
    if sum(list_n[i:j]) >= s:
      if len(list_n[i:j]) < min_length:
        min_length = len(list_n[i:j])

print(min_length)
