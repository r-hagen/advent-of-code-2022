import heapq

lines = [line.strip() for line in open('d12.in').readlines()]

S = (0, 0)
E = (0, 0)
G = [[0] * len(line) for line in lines]

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'S':
            S = (x, y)
            G[y][x] = ord('a') - ord('a')
        elif char == 'E':
            E = (x, y)
            G[y][x] = ord('z') - ord('a')
        else:
            G[y][x] = ord(char) - ord('a')

paths = [(0, S[0], S[1])]
vis = [[0]*len(row) for row in lines]

while True:
    s, x, y = heapq.heappop(paths)
    if vis[y][x]: 
        continue
    if (x, y) == E:
        print(s)
        break
    vis[y][x] = 1
    for nx, ny in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
        if not len(G[0]) > nx >= 0 <= ny < len(G):
            continue
        if not G[ny][nx] <= G[y][x] + 1:
            continue
        if vis[ny][nx]: 
            continue
        heapq.heappush(paths, (s+1, nx, ny))

