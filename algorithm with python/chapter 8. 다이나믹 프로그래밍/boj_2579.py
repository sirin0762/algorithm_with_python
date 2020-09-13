# 계단 오르기
# 3번 연속으로는 못오름
# 계단의 점수 최대값

n = int(input())

arr = [int(input()) for _ in range(n)]

max_values = [0] * n

max_values[0] = arr[0]
max_values[1] = max_values[0] + arr[1]

for i in range(2, n):
  max_values[i] = max(arr[i] + max_values[i - 2], max_values[i - 3] + arr[i - 1] + arr[i], max_values[i - 1]) 

print(max_values[n - 1])