# 특정 도시에서 연결된 도시 개수와, 가장 먼 길이를 구해라

import heapq

INF = int(1e9)

v, e, start = map(int, input().split())

graph = [[] for _ in range(v + 1)]

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

distance = [INF] * (v + 1)

print(distance)

def dijkstra(start):
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0
for i in distance:
  if i != INF:
    count += 1
    max_distance = max(i, max_distance)

print(count - 1, max_distance)