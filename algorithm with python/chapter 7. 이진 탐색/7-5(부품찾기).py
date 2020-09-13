# 문제 : 가게 부품이 총 5개일 때 손님이 말한 3개의 부품이 다 있는지 확인하자.

# 이진 탐색으로 문제풀이
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

n = int(input())
product = list(map(int, input().split()))
product.sort()

m = int(input())
request = list(map(int, input().split()))

for i in request:
    result = binary_search(product, i, 0, n-1)
    if result != None:
        print('yes')
    else:
        print('no')
        