# RGB 거리
# 난이도 중 상
# 내 실패 요인 : 점화식을 구하지 못함, 동적 프로그래밍 방식으로 연결 실패

# 집을 칠 할 색깡은 그 전의 집의 색깔에 의해 결정되므로

import sys

n = int(input())

datas =[[0, 0, 0] for _ in range(n)]

for i in range(n):
  temp = list(map(int, sys.stdin.readline().split()))

  if i == 0:
    datas[0] = temp

  else:
    datas[i][0] = min(datas[i - 1][1], datas[i - 1][2]) + temp[0]
    datas[i][1] = min(datas[i - 1][0], datas[i - 1][2]) + temp[1]
    datas[i][2] = min(datas[i - 1][0], datas[i - 1][1]) + temp[2]

print(min(datas[n - 1]))
