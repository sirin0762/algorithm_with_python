# 문자열 뒤집기 : 연속된 문자열만 뒤집을 수 있다
# 모두가 1 or 0 이 나오도록 최소의 횟수로 문자열을 뒤집어라

n = input()

answer = []
slice = 0

for i in range(len(n)):
  if i < len(n) - 1:
    if n[i] != n[i + 1]:
      answer.append(n[slice:i + 1])
      slice = i + 1

if n[slice:]:
  answer.append(n[slice:])

zero = 0
one = 0
for i in answer:
  if '0' in i:
    zero += 1
  elif '1' in i:
    one += 1

if zero < one:
  print(zero)
else:
  print(one)

