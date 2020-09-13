# 문제 : N 개의 정수가 주어져 있을 때, 이 안에 x 라는 정수가 존재하는지 알아내는 프로그램을 작성하시오


# input
n = int(input())
list_of_int = list(map(int, input().split()))
m = int(input())
comparison_target = list(map(int, input().split()))

# 이진 탐색
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
      return True
    
    elif array[mid] > target:
      end = mid - 1
    
    else:
      start = mid + 1
  
  return False

# 데이터 정렬
list_of_int.sort()

for target in comparison_target:
  print(binary_search(list_of_int, target, 0, n -1 ))