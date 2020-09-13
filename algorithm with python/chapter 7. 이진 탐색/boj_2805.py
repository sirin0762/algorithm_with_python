# 1. 절단기 높이 지정
# 2. 잘린 나무 더하기
# 3. 맞는지 아닌지 확인

n, m = map(int, input().split())

trees = list(map(int, input().split()))

end = max(trees)

def binary_search(array, target, start, end):

  while start <= end:
    mid = (start + end) // 2
    sum_cutted_trees = 0

    for i in trees:
      if i - mid > 0:
        sum_cutted_trees += (i - mid)

    if target == sum_cutted_trees:
      return mid

    elif target > sum_cutted_trees:
      end = mid - 1

    else:
      start = mid + 1

  return mid

print(binary_search(trees, m, 0, end)) 