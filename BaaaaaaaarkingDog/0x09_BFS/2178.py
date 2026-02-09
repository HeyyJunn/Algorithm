import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(row)]
vis = [[0] * col for _ in range(row)]
dist = [[-1] * col for _ in range(row)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

dq = deque()

vis[0][0] = 1
dist[0][0] = 1
dq.append((0,0))

while dq:
  cur = dq.popleft()
  r, c = map(int, cur)
  save_dist = dist[r][c]


  for dir in range(4):
    next_r = r + dr[dir]
    next_c = c + dc[dir]
  
    if next_r < 0 or next_r >= row or next_c < 0 or next_c >= col: continue
    if vis[next_r][next_c] == 1 or board[next_r][next_c] == 0: continue
    
    vis[next_r][next_c] = 1
    dq.append((next_r, next_c))

    dist[next_r][next_c] = save_dist + 1

print(dist[row - 1][col - 1])
