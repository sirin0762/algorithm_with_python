# 숫자로 이루어진 피라미드에서 최대 값을 구하시오.


n = int(input())

arr = []
d = []

for i in range(n):
  line = list(map(int, input().split()))
  arr.append(line)
  d.append([0] * len(line))

d[0][0] = arr[0][0]

d[1][0] = d[0][0] + arr[1][0]
d[1][1] = d[0][0] + arr[1][1]

for i in range(2, n):
  for j in range(len(arr[i])):
    print(i, j)
    # 좌측 빗변
    if j == 0:
      d[i][j] = d[i - 1][j] + arr[i][j]
    
    # 가운데 부분
    elif j == len(arr[i]) - 1:
      d[i][j] = d[i - 1][j - 1] + arr[i][j]

    # 우측 빗변
    else:
      d[i][j] = max(d[i - 1][j], d[i - 1][j - 1]) + arr[i][j]
  
  # 한 줄의 max 값
  max_value = max(d[i])

print(max_value)