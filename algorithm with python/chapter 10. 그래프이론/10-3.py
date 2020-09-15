# 경로 압축 방법을 적용한 서로소 집합 

# 루트노드 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 부모끼리 연결 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('집합 : ', end = '')
for i in range(1, v + 1):
    # parent를 그냥 쓰면 안되는 이유 : union_parent 함수는 연결만 해주지 루트노드까지 보여주지 않는다.
    # 따라서 find 함수를 통해 루트노드를 찾아야한다.
    print(find_parent(parent, i), end = '')

print()

# 부모 테이블 출력
# 112155 가 아닌 111155 가 출력되는 이유 : 위의 for문에서 find 함수를 통해 부모테이블이 루트 노드를 가리키게 끔 바꿈
print('부모테이블 : {}'.format(parent[1:]))
