# 7-5와 같은 문제를 계수 정렬을 이용하여 풀이

n = int(input())
array = [0] * 1000000

for i in input().split():
    array[int(i)] = 15 

m = int(input())
request = list(map(int, input().split()))

for i in request:
    if array[int(i)]:
        print('yes')
    else:
        print('no')