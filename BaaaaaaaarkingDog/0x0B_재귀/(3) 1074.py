import sys
input = sys.stdin.readline

# N: 가로 세로의 크기
# r 행
# c 열
# N 이 주어졌을 때, r행 c열을 몇번째로 방문하는지를 출력

# N = k 일 때 결과를 가지고, N = k+1 일 때의 결과를 구할 수가 있음
# 함수의 정의
# 2^n x 2^n 배열에서 (r,c) 를 방문하는 순서를 반환하는 함수

def printZ(N, r, c):
  half = 2**(N-1)  # base condition
  if N == 0: return 0
  # 1사분면
  if r < half and c < half:
      return printZ(N - 1, r, c)
  # 2사분면q
  elif r < half and c >= half:
      return half * half + printZ(N - 1, r, c - half)
  # 3사분면
  elif r >= half and c < half:
      return 2 * half * half + printZ(N - 1, r - half, c)
  # 4사분면
  else:
      return 3 * half * half + printZ(N - 1, r - half, c - half)

N, r, c = map(int, input().split())
# arr = [[0] * c for _ in range(r)]
print(printZ(N, r, c))