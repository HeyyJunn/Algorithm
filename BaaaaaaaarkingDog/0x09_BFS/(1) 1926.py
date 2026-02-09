import sys
from collections import deque
input = sys.stdin.readline
# 1. 상하좌우로 연결된 그림의 크기를 알아내기
# 2. 도화지에 있는 모든 그림을 찾아내기

row, col = map(int, input().split())
dq = deque()
dx = [1, 0, -1, 0] 
dy = [0, 1, 0, -1]

board = [[0]*col for _ in range(row)] # 보드
# board = [list(map(int, input().split())) for _ in range(row)]
vis = [[0]*col for _ in range(row)] # 방문여부

for r in range(row): # 보드정보입력
  board[r] = list(map(int, input().split()))
count = 0 # 그림 갯수 출력용
max_area = 0

for r in range(row): # 이중 for 문으로 시작점 탐색
  for c in range(col):
    if vis[r][c] == 0 and board[r][c] == 1: # 방문되지 않았고, board 의 값이 1 일 때
      area_count = 1
      vis[r][c] = 1 # 방문으로 변경하고
      dq.append((r, c)) # 큐에 해당 좌표값을 추가

      while(dq): # 큐가 빌 때 까지
        cur = dq.popleft() # 현재 큐 값을 pop 시키고, 반환값을 cur 변수에 저장
        # x, y = dq.popleft()
        # 로 언패킹 해도 가능
        
        for dir in range(4): # 상하좌우로 탐색  
          nx = cur[0] + dx[dir]
          ny = cur[1] + dy[dir]
          # 상하좌우 탐색을 위한 x, y 값이 범위를 넘어갈 때 continue
          if nx < 0 or nx >= row or ny < 0 or ny >= col:
            continue
          # 만약 이미 방문되었거나, 보드 값이 1 이 아닐 때 continue
          if vis[nx][ny] == 1 or board[nx][ny] != 1:
            continue
          # 방문처리 하고, 큐에 append(연쇄적으로 탐색하기 위함), 넓이 +1
          vis[nx][ny] = 1
          dq.append((nx, ny))
          area_count += 1
      count += 1
      max_area = max(max_area, area_count)

print(count)
print(max_area if count != 0 else 0)





