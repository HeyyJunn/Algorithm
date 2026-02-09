import sys
from collections import deque
input = sys.stdin.readline

col, row = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]
dist = [[0] * col for _ in range(row)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

dq = deque()

max_dist = 0

for r in range(row):
  for c in range(col):
    if board[r][c] == 1:
      dq.append((r,c))
    if board[r][c] == 0:
      dist[r][c] = -1

while dq:
  ###################################
  cur_r, cur_c = dq.popleft()
  # print(f"debug: {cur_r} {cur_c}")

  for dir in range(4):
    next_r = cur_r + dr[dir]
    next_c = cur_c + dc[dir]

    if next_r < 0 or next_r >= row or next_c < 0 or next_c >= col:
      continue
    if board[next_r][next_c] != 0:
      continue

    dq.append((next_r, next_c))
    board[next_r][next_c] = 1
    dist[next_r][next_c] = dist[cur_r][cur_c] + 1
    # print(f"debug: dist = {dist[next_r][next_c]}")

for r in range(row):
  for c in range(col):
    if dist[r][c] == -1:
      print("-1")
      sys.exit()
    else:
      max_dist = max(max_dist, dist[r][c])

print(max_dist)



      

############################################

###################################
# print(f"debug{col} {row}")
# for i in range(row):
#   print(board[i])