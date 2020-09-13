# 문제 유형 : binary_search

n = int(input())

sang_cards = list(map(int, input().split()))

m = int(input())

ints = list(map(int, input().split()))

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

sang_cards.sort()

for i in ints:
  if binary_search(sang_cards, i, 0, n - 1):
    print('1')
  else:
    print('0')