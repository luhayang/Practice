import sys

n = int(sys.stdin.readline())
result = []

def check():
    length = len(result)
    for i in range(1, length//2 +1):
        if result[-i:] == result[-2*i : -i]:
            return False
    return True

def backTracking(idx):
    if idx == n:
        print(*result, sep='')
        sys.exit(0)

    for i in range(1, 4):
        result.append(i)
        if check():
            backTracking(idx+1)
        result.pop()

backTracking(0)