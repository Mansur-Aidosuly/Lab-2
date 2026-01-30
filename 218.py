n = int(input())
arr = []

for _ in range(n):
    arr.append(input().strip())

first_index = {}

# Store first occurrence of each string
for idx, s in enumerate(arr, start=1):
    if s not in first_index:
        first_index[s] = idx

# Print in lexicographical order
for s in sorted(first_index):
    print(s, first_index[s])
