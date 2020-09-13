import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())
print(start)

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        # 이미 방문한적 있는지 확인
        # dist 는 최단 경로는 아니므로 이미 최단 경로가 나왔으면 필요없는 단계이니 continue로 스킵
        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")

    else:
        print(distance[i])
