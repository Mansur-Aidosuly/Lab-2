size, l, r = map(int, input().split())
numbers = list(map(int, input().split()))

# convert to 0-based indexing
l -= 1
r -= 1

while l < r:
    numbers[l], numbers[r] = numbers[r], numbers[l]
    l += 1
    r -= 1

print(*numbers)
