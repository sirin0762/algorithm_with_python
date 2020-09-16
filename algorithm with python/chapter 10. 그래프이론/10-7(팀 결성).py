# 두 가지 연산
# 1. 만약 boolean 이 1 이면 a, b가 같은 팀인지 출력
# 2. boolean이 0이면 a, b 를 같은 팀으로


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  
  return parent[x]

def check_team(a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a == b:
    print('YES')
  else:
    print('No')

v, e = map(int, input().split())

parent = [0] * (v + 1)

for i in range(1, v + 1):
  parent[i] = i

for _ in range(e):
  boolean, a, b = map(int, input().split())
  if boolean:
    check_team(a, b)
  else:
    union_parent(parent, a, b)

 