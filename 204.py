n = int(input())
numbers = list(map(int, input().split()))

pos = 0

for i in numbers:
    if i > 0:
        pos += 1
print(pos)