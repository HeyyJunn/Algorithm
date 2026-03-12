import sys
input = sys.stdin.readline

def hanoi(n, start, bypass, end):

  if (n == 1): 
    print(f"{start} {end}") # Base condition
    return

  hanoi(n-1,start, end, bypass)
  print(f"{start} {end}")
  hanoi(n-1, bypass, start, end)
  return  

N = int(input())

print(2**N -1)
hanoi(N, 1, 2, 3)


