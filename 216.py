n = int(input())
numbers = list(map(int, input().split()))

newbie = set()

for i in numbers:
    if i in newbie:
        print("NO")
    else:
        print("YES")
        newbie.add(i)    