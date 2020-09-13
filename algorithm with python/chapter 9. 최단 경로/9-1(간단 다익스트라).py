# 간단한 다익스트라 알고리즘 소스코드

import sys
# 더 빠른 input인 sys.readline으로 치환
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n + 1)]

visited = [False] * (n + 1)

distance = [INF] * (n + 1)

for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
    for j in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        
        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    # 도달 할 수 없는 경우, 무한 이라고 출력
    if distance[i] == INF:
        print('INFINITY')
    
    else:
        print(distance[i])