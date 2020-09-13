# 최단경로의 미로 -> 벽을 뚫는 것이 가능, 최소의 벽을 뚫어서 통과해라
# bfs, 다익스트라 알고리즘 2가지 중 선택하는게 현명해보임

# 1. 다익스트라 : 결국 가중치를 가진 그래프의 최단 경로를 구하는 방식
# 알아야 할 점 : 지금까지는 linkedgraph 일 때 푸는 방식을 배웠다면 이번 문제는 arraylist_graph 임

import heapq

INF = int(1e9)

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

distance = [[INF] * m for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dijkstra(x, y):
    q = []
    distance[x][y] = 0
    heapq.heappush(q, (distance[x][y], x, y))

    while q:
        dist, pop_x, pop_y = heapq.heappop(q)

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            nd = dist + graph[nx][ny]
            if distance[nx][ny] > nd:
                distance[nx][ny] = nd
                heapq.heappush(q, (nd, nx, ny))
    
    return distance[n - 1][m - 1]

print(dijkstra(0, 0))

# # 2. bfs
# # deque의 앞 뒤로 넣는 속성을 이용하여 우선순위가 있는 큐를 구현(벽이 있으면 왼쪽, 벽이 없으면 오른쪽으로 넣음)
# def bfs():
#     dq = deque()
#     dq.append((0, 0))
#     a[0][0] = -1
#     while dq:
#         x, y = dq.pop()
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if a[nx][ny] == -1:
#                 continue
#             elif a[nx][ny] == 0:
#                 d[nx][ny] = d[x][y]
#                 dq.append((nx, ny))
#             else:
#                 d[nx][ny] = d[x][y] + 1
#                 dq.appendleft((nx, ny))
#             a[nx][ny] = -1
#     return d[n-1][m-1]

# print(bfs())


# 출처: https://rebas.kr/657 [PROJECT REBAS]