import sys
input = sys.stdin.readline

def hanoi(n, start, bypass, end):

  if (n == 1): 
    print(f"{start} {end}") # Base condition
    return

  hanoi(n-1,start, end, bypass) 
  # 위에 있는 n-1개를 start에서 bypass로 옮김.
  # 원판 n-1개를 start에서 bypass로 옮기는 데 필요한 모든 이동을 전부 출력해라
  print(f"{start} {end}") # 가장 큰 원판 1개를 start -> end로 옮기는 것.
  hanoi(n-1, bypass, start, end) # 아까 bypass에 잠깐 옮겨놨던 n-1개를 end로 옮김.
  return  

N = int(input())

print(2**N -1)
hanoi(N, 1, 2, 3)


