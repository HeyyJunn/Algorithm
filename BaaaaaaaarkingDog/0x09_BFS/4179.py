import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(r)]

fire_dq = deque()
j_dq = deque()

j_time_count = []

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

j_board = [[-1] * c for _ in range(r)]

for row in range(r):
  for col in range(c):
    if board[row][col] == "J":
      j_board[row][col] = 0
      j_dq.append((row, col))
    if board[row][col] == "F":
      fire_dq.append((row, col))

while j_dq:
  fire_len = len(fire_dq)
  for _ in range(fire_len):
      fire_r, fire_c = fire_dq.popleft()
      for dir in range(4):
          fire_nr = fire_r + dr[dir]
          fire_nc = fire_c + dc[dir]
          if fire_nr < 0 or fire_nr >= r or fire_nc < 0 or fire_nc >= c:
              continue
          if board[fire_nr][fire_nc] != ".":
              continue
          board[fire_nr][fire_nc] = "F"
          fire_dq.append((fire_nr, fire_nc))

  j_len = len(j_dq)
  for _ in range(j_len):
    j_r, j_c = j_dq.popleft()
    cur_t = j_board[j_r][j_c]
    for dir in range(4):
      j_nr = j_r + dr[dir]
      j_nc = j_c + dc[dir]

      if j_nr < 0 or j_nr >= r or j_nc < 0 or j_nc >= c:
          print(cur_t + 1)
          sys.exit()
      if board[j_nr][j_nc] != ".":
        continue
      if j_board[j_nr][j_nc] != -1:
        continue
    
      j_dq.append((j_nr, j_nc))
      j_board[j_nr][j_nc] = j_board[j_r][j_c] + 1

print("IMPOSSIBLE")

###################################
# print(f"debug: {}")