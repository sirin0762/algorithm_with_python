# 나의 문제 풀이

# 1. 절단기 높이 맞추기
# 2. 떡 자르기
# 3. 자른 떡 길이 비교하기

# n, total_length = map(int, input().split())

# lengths = list(map(int, input().split()))

# temp = max(lengths)
# cutted = 0

# while temp >= 0:
#   for i in lengths:
#     if (i - temp) > 0:
#       cutted += (i - temp)

#   if cutted >= total_length:
#     break  
  
#   temp -= 1
#   cutted = 0

# print(temp)

# 문제 해설

# 절단기의 위치를 계속 조절하면서(binary_search) 떡의 길이를 비교한다.

n, length = map(int, input().split())

array = list(map(int, input().split()))

result = 0
start = 0
end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x > mid:
            total += x - mid
    
    if total < length:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    
print(result)