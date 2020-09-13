#순차 탐색 - 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서 부터 하나씩 데이터를 확인 하는 탐색 방법. 가장 기초적이고 직관적이다.
#순차 탐색은 보통 정렬되지 않은 데이터들 중에서 찾을 때 사용된다.

#순차 탐색은 앞에서 부터 하나씩 확인 하기 때문에 최악의 복잡도는 O(N) 이다.

#7-1.py 순차 탐색 소스 코드
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1 # 현재의 위치 반환(index + 1)

print('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.')
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print('앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.')
array = input().split()

print(sequential_search(n,target, array))