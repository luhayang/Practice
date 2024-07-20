import sys
from collections import deque

def bfs(queue, maze, dx, dy):
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nX, nY = x+dx[i], y+dy[i]
            if 0 <= nX < n and 0 <= nY < m:
                if maze[nX][nY] == 1:
                    queue.append((nX, nY))
                    maze[nX][nY] = maze[x][y]+1

    return maze[n-1][m-1]

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    maze = [list(map(int, ' '.join(sys.stdin.readline().split()))) for _ in range(n)]
    
    queue = deque([(0,0)])

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    print(bfs(queue, maze, dx, dy))