n = int(input())
nums = list(map(int, input().split()))

result = list(map(lambda x: x ** 2, nums))

print(*result)