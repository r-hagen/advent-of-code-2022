import re

top, bottom = open('d22.in').read().split('\n\n')

grid = []

for line in top.split('\n'):
    grid.append(line)

width = max(map(len, grid))
grid = [line + ' ' * (width - len(line)) for line in grid]

r = 0
c = grid[r].index('.')
dr = 0
dc = 1

for x, y in re.findall(r'(\d+)([RL]?)', bottom):
    x = int(x)
    for _ in range(x):
        nr = r
        nc = c
        while True:
            nr = (nr + dr) % len(grid)
            nc = (nc + dc) % len(grid[0])
            if grid[nr][nc] != ' ':
                break
        if grid[nr][nc] == '#':
            break
        r = nr
        c = nc
    if y == 'R':
        dr, dc = dc, -dr
    elif y == 'L':
        dr, dc = -dc, dr

if dr == 0:
    if dc == 1:
        k = 0
    else:
        k = 2
else:
    if dr == 1:
        k = 1
    else:
        k = 3

print(1000 * (r + 1) + 4 * (c + 1) + k)
