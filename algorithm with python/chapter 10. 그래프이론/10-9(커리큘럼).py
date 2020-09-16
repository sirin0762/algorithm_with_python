# 위상정렬(topology algorithm)
# 리스트의 경우 단순히 대입 연산을 하면 값이 변경 될 때 문제가 발생 할 수 있기 때문에, 리스트의 값을 복제할 때는 deepcopy() 함수를 이용한다.
from collections import deque
import copy

n = int(input())

graph = [[] for i in range(n + 1)]
time = [0] * (n + 1)
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])

topology_sort()

            