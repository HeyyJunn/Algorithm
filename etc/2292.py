import sys
input = sys.stdin.readline

n = int(input())

end = 1
layer = 1

while end < n:
  end += 6 * layer
  layer += 1

print(layer)