n = int(input())

freq = {}

for _ in range(n):
    number = input().strip()
    freq[number] = freq.get(number, 0) + 1

count = 0

for v in freq.values():
    if v == 3:
        count += 1

print(count)