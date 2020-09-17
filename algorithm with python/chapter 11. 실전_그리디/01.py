# 모험가 길드
# 공포도가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력 부족   
# 모험가 동빈이는 모험가 그룹을 모음   
# 공포도 X 이상의 인원은 x명의 그룹을 이뤄야함
# 주어진 맴버중 그룹이 가능한 개수

n = int(input())
members = list(map(int, input().split()))

members.sort()

answer = [[] for _ in range(n + 1)]
cnt = 0

for i in members:
  answer[i].append(i)

for idx, j in enumerate(answer):
  if j:
    cnt += len(j) // idx

print(cnt)