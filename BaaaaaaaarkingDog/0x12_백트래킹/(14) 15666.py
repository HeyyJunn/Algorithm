import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = list(map(int, input().split()))
board.sort()
path = []

def backtrack():
  if len(path) == M:
    print(* path)
    return
  prev = None
  for x in range(N):
    if prev == board[x]: continue
    if path and path[-1] > board[x]: continue
    prev = board[x]
    path.append(board[x])
    backtrack()
    path.pop()

backtrack()
