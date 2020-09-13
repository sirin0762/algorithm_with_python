# 7-5와 같은 문제를 set 구조를 이용하여 파악(간결함 최고)

n = int(input())
product = set(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

for i in request:
    if i in product:
        print('yes')
    else:
        print('no')