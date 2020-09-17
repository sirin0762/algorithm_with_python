# 만들 수 없는 금액
# 1,2,3 -> 1 ~ 6 까지
# 1,2,3,5 -> 1 ~ 11 까지
# 1,2,3,5,10 -> 1 ~ 21 까지
# 특정 target 이 동전 보다 작으면 -> answer
# target은 계속 업데이트 됨

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
  if target < x:
    break
  target += x

print(target)