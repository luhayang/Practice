import sys

def Josephus(queue, k):
    result = list()
    num = k-1
    for i in range(len(queue)):
        if (len(queue) > num):
            result.append(queue.pop(num))
            num += k-1
        else:
            num = num%len(queue)
            result.append(queue.pop(num))
            num += k-1
    return result

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    queue = list()
    for i in range(1, n+1):
        queue.append(i)
    result = Josephus(queue, k)
    print(f"<{', '.join(map(str, result))}>")