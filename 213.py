m = int(input())
count = 0
for i in range(1, m):
    if m % i == 0:
        count = count + 1

if count <= 1:
    print("Yes")
else:
    print("No")    

