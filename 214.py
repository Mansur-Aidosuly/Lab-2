n = int(input())
numbers = list(map(int, input().split()))

freq = {}

for x in numbers:
    freq[x] = freq.get(x, 0) + 1


max_freq = 0
answer = None

for key, value in freq.items():
    if value > max_freq or (value == max_freq and key < answer):
        max_freq = value
        answer = key

print(answer)