# 합집합 연산
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])

  return x


# 노드, 간선 입력
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블 초기화
for i in range(1, v + 1):
  parent[i] = i

# union 연산을 각각 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

print('각 원소가 속한 집합 : ', end = '')
for i in range(1, v + 1):
  print(find_parent(parent, i), end = '')

print()

print('부모 테이블 : ', end = '')
for i in range(1, v + 1):
  print(parent[i], end = '')
