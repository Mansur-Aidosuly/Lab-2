n = int(input())
document = {}

for _ in range(n):
    cmd = input().strip().split()
    if cmd[0] == "set":
        key = cmd[1]
        value = cmd[2]
        document[key] = value

    elif cmd[0] == "get":
        key = cmd[1]
        if key in document:
            print(document[key])
        else:
            print(f"KE: no key {key}")