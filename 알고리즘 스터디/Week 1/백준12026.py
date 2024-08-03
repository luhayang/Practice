import sys

n = int(sys.stdin.readline())
blocks = sys.stdin.readline().strip()

INF = float('inf')
dp = [INF]*n
dp[0] = 0

next = {'B': 'O', 'O': 'J', 'J': 'B'}

for i in range(n):
    for j in range(i+1, n):
        if blocks[j] == next[blocks[i]]:
            cost= (j-i) ** 2
            dp[j] = min(dp[j], dp[i] + cost)

print(dp[-1] if dp[-1] != INF else -1)