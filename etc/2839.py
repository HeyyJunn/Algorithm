import sys
input = sys.stdin.readline

n = int(input())

five = n // 5
ans = -1

while five >= 0:
  remain = n - five * 5
  if remain % 3 == 0:
    three = remain // 3
    ans = five + three
    break
  five -= 1

print(ans) 
