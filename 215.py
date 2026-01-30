n = int(input())

names = set()

for _ in range(n):
    name = input().strip()
    names.add(name)

print(len(names))