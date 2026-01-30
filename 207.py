n = int(input())
numbers = list(map(int, input().split()))
position = 1
maxval = numbers[0]
for i in range(1, n):
    current = numbers[i]
    if current > maxval:
        maxval = current
        position = i + 1
print(position)        