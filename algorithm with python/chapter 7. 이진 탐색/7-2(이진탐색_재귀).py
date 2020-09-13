# 이진탐색 : 찾으려는 데이터가 이미 정렬되어 있어야지 사용 가능, 무작위에서는 불가능

# 이진 탐색은 위치를 나타내는 변수 3개를 사용(시작, 끝, 중간) 이 3개의 변수를 옮기면서 탐색하는 방식. 찾으려는 데이터와 중간지점에 있는 데이터를 반복적으로 비교해서 데이터를 찾음.
# 정리 : 시작점 끝점 = 범위, 중간점 = 비교

# step 1 : 시작점과 끝점을 확인한 다음 둘 사이의 중간점을 정한다. 중간점이 실수일 때는 소수점 이하를 버린다. 중간점과 데이터를 비교하고, 데이터가 작으면 오른쪽, 크면 왼쪽을 버린다(오름차순 기준).
# 시작점 or 끝점을 옮긴다
# step 2 : 다시 중간점을 매칭하고,  step 1을 반복한다.
# step 3 : step 1, step 2를 반복한다. 

# 복잡도는 O(log N)

# 제대로 이진 탐색 코드를 작성한 프로그래머는 10% 내외라 할 정도로 실재 구현은 까다롭다. 코드가 짧으니 이진 탐색을 처음 접했다면, 여러차례 코드를 입력하며 자연스럽게 외워보자.

# 7-2.py : 재귀 함수로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 찾은 경우 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 데이터가 작으면 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid + 1, end)

#원소의 개수와 target 입력
n, target = list(map(int, input().split()))

# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)

