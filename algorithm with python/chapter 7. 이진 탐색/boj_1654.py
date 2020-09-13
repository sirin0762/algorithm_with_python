# N개의 렌선
# K개의 랜선 -> 제각각
# k의 렌선을 잘라서 N 개의 렌선 최대 길이

k, n = map(int, input().split())

lan_list = [int(input()) for _ in range(k)]

arr = [x for x in range(1, 10001)]

def binary_search(array, target, start, end):
  result = 0

  while start <= end:
    mid = (start + end) // 2  
    count = 0

    for i in lan_list:
      count = count + (i // array[mid])

    if count == target:
      if array[mid] > result:
        result = array[mid]
        start = mid + 1
      

    elif count < target:
      end = mid - 1

    else:
      result = array[mid]
      start = mid + 1
  
  return result

print(binary_search(arr, 11, 0, len(arr) - 1))