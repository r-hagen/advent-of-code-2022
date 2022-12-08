G = [list(map(int, line.strip())) for line in open('d08input.txt').readlines()]
rows = len(G)
cols = len(G[0])


def scenic_score(r, c):
    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
        return 0
    h = G[r][c]

    x = r - 1
    while x > 0 and h > G[x][c]: x -= 1
    up = r - x

    x = r + 1
    while x < rows - 1 and h > G[x][c]: x += 1
    down = x - r

    x = c - 1
    while x > 0 and h > G[r][x]: x -= 1
    left = c - x

    x = c + 1
    while x < cols - 1 and h > G[r][x]: x += 1
    r = x - c

    return up * down * left * r


print(max([scenic_score(r, c) for r in range(rows) for c in range(cols)]))
