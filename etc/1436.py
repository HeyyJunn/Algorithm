import sys
input = sys.stdin.readline

n = int(input())

start = 666
count = 0

while count != n:
  if str(666) in str(start):
    count += 1
  start += 1

print(start - 1)
