from collections import deque

n = int(input())
maps = [[0] * (n + 1) for _ in range(n + 1)]

k = int(input())
for _ in range(k):
  a, b = map(int, input().split())
  maps[a][b] = 1

l = int(input())
data = []
sum_value = 0
for i in range(l):
  if i:
    distance, direction = input().split()
    data.append([int(distance) - sum_value, direction])
    sum_value = int(distance)
  else:
    distance, direction = input().split()
    data.append([int(distance) , direction])
    sum_value = int(distance)

data.append([int(1e9), 'D'])

print(data)
# 북 동 남 서
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
dire = 1

snake = deque()
snake.append((1, 1))

def sol():
  global dire
  count = 0
  for d in data:
    for _ in range(d[0]):
      count += 1
      x, y = snake.pop()
      nx, ny = x + dx[dire], y + dy[dire]

      # 벽에 부딪히면 종료
      if nx > n + 1 or ny > n + 1 or nx <= 0 or ny <= 0:
        print('wall', nx, ny)
        return count

      # 뱀의 몸통에 부딪히면 종료
      if (nx, ny) in snake:
        print('snake', nx, ny)
        return count

      # 뱀의 이동, 사과 없을 때
      if maps[nx][ny] == 0:
        snake.append((x, y))
        snake.append((nx, ny))
        snake.popleft()
      
      # 사과 있을 때
      elif maps[nx][ny] == 1:
        snake.append((x, y))
        snake.append((nx, ny))

      print(nx, ny)

    if d[1] == 'D':
      dire = (dire + 1) % len(dx)
    
    elif d[1] == 'L':
      dire = (dire + 3) % len(dx)
  return count

print(sol())