n = int(input())
numbers = list(map(int, input().split()))

length = len(numbers)
for i in range(length):
    for j in range(0, n - i - 1):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

for i in numbers:
    print(i, end = " ")