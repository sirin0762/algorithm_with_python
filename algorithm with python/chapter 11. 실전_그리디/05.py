# 볼링공 고르기
# 서로 다른 무게의 볼링공을 고르시오

n, m = map(int, input().split())

balls = list(map(int, input().split()))

balls.sort()

slice = 0
cnt = 0
for i in range(n):
    for j in balls[:slice] + balls[slice:]:
        if balls[i] != j:
            cnt += 1

print(cnt // 2)