import sys
input = sys.stdin.readline

paper_counts = [0, 0, 0]

def count_papers(size, x, y, board):

  # size == 1 이면 무조건 check return True
  # if size == 1:
  #   if board[x][y] == -1: paper_counts[0] += 1
  #   elif board[x][y] == 0: paper_counts[1] += 1
  #   else: paper_counts[2] += 1
  #   return

  new_size = size // 3

  if not check(size, x, y, board):
    for dx in [0, new_size, 2 * new_size]:
      for dy in [0, new_size, 2 * new_size]:
        count_papers(new_size, x+dx, y+dy, board)

    # count_papers(new_size, x, y, board)
    # count_papers(new_size, x + new_size, y, board)
    # count_papers(new_size, x + 2*new_size, y, board)

    # count_papers(new_size, x, y+new_size, board)    
    # count_papers(new_size, x + new_size, y+new_size, board)  
    # count_papers(new_size, x + 2*new_size, y+new_size, board)
    
    # count_papers(new_size, x, y+2*new_size, board)    
    # count_papers(new_size, x+new_size, y+2*new_size, board)    
    # count_papers(new_size, x+2*new_size, y+2*new_size, board)   

  else:
    paper_counts[board[x][y] + 1] += 1

def check(size, x, y , board):
  point = board[x][y]
  for i in range(size):
    for j in range(size):
      if board[x+i][y+j] != point: return False
  return True

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# print(board)
count_papers(N, 0, 0, board)

for x in paper_counts:
  print(x)