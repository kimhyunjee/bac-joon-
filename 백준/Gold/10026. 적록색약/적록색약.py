import sys

sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 색을 따로 변수로 저장하여 이동할 칸의 색과 비교
def dfs(x, y):
    visited[y][x] = True
    color = grid[y][x]
    for dx, dy in d:
        X, Y = x + dx, y + dy
        if (0 <= X < N) and (0 <= Y < N):
            if visited[Y][X] == False and grid[Y][X] == color:
                dfs(X, Y)

# 적록색맹이 아닐 경우
cnt, cnt2 = 0, 0

for y in range(N):
    for x in range(N):
        if visited[y][x] == False:
            dfs(x, y)
            cnt += 1
            
# 초록-> 빨강으로 수정 / 방문 리스트를 재사용하기 때문에 초기화
for y in range(N):
    for x in range(N):
        if grid[y][x] == 'G':
            grid[y][x] = 'R'
visited = [[False] * N for _ in range(N)]

# 적록색맹일 경우
for y in range(N):
    for x in range(N):
        if visited[y][x] == False:
            dfs(x, y)
            cnt2 += 1

print(cnt, cnt2)