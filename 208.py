n = int(input())
a = 1
arr = []
while a <= n:
    arr.append(a)
    a *= 2
for i in arr:
    print(i, end = " ")
     