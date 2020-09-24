s = input()

result = []

for i in range(1, len(s)):
  # 문자열을 자름
  data = [s[x:x + i] for x in range(0, len(s), i)]
  count = 1
  narrow_str = ''
  # 문자열을 더함
  for j in range(len(data)):
    # data의 마지막 인덱스 일 때

    if j == len(data) - 1:
      if count == 1:
        narrow_str += data[j]
      else:
        narrow_str += str(count) + data[j]
      break
    
    if data[j] == data[j + 1]:
      count += 1
      continue
    
    else:
      if count == 1:
        narrow_str += data[j]
      else:
        narrow_str += str(count) + data[j]
      
      count = 1
    
  result.append(len(narrow_str))

print(min(result))

    