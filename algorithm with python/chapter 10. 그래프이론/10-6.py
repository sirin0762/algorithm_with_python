from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1)

graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
  result = [] # 알고리즘 수행 결과를 담을 리스트
  q = deque() # 큐 기능을 위한 deque 라이브러리 사용

  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, v + 1):
    if indegree[i]:
      q.append(i)

  # 큐가 빌때 까지 반복
  while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
      indegree[i] -= 1

      if indegree[i] == 0:
        q.append(i)

  for i in result:
    print(i)

topology_sort()