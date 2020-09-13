INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int , input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘(다이나믹 프로그래밍)
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # A -> B = min(A->B, A -> k + K -> B)
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('INFINITY')

        else:
            print(graph[a][b])

    print()


