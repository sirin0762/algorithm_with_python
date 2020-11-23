# 큰 수의 법칙
# 나의 해답
n, m, k = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort(reverse = True)

result = (k * arr[0]) * (m // k) + (m - (k * (m // k))) * arr[1]
print(result)
