import sys
input = sys.stdin.readline

count_colors = [0, 0]

def count_papers(N, x, y, board):
  new_size = N // 2

  if not check_bool(N, x, y, board):
    for dx in [0, new_size]:
      for dy in [0, new_size]:
        count_papers(new_size, x + dx, y + dy, board)
  else:
    count_colors[board[x][y]] += 1 
    return

def check_bool(N, x, y, board):
  point = board[x][y]
  for i in range(N):
    for j in range(N):
      if board[x + i][y + j] != point: return False
  return  True

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# print(f"debug: {board}")
count_papers(N, 0, 0, board)

for x in count_colors:
  print(x)