n = int(input())
numbers = list(map(int, input().split()))

minVal = min(numbers)
maxVal = max(numbers)

upd_Numbers = []

for x in numbers:
    if x == maxVal:
        upd_Numbers.append(minVal)
    else:    
        upd_Numbers.append(x) 

for i in upd_Numbers:
    print(i, end = " ")        
