import sys
input = sys.stdin.readline

# a ^ b mod c 를 반환하는 함수
def func1 (a, b, c):
  if b == 1:
    return a % c
  val = func1(a, b//2, c)
  val = val * val % c
  if (b % 2 == 1):
    return val * a % c
  return val

a, b, c = map(int, input().split())
print(func1(a, b, c))
# print(f"debug: {a, b ,c}")






