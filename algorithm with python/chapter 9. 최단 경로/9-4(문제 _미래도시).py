INF = int(1e9)

v, e = map(int, input().split())

graph = [[INF] * (v + 1) for _ in range(v + 1)]

for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print('-1')
else:
    print(distance)