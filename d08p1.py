G = [list(map(int, line.strip())) for line in open('d08input.txt').readlines()]
rows = len(G)
cols = len(G[0])


def visible(r, c):
    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
        return True
    h = G[r][c]
    t = all([h > G[x][c] for x in range(0, r)])
    b = all([h > G[x][c] for x in range(r + 1, rows)])
    l = all([h > G[r][x] for x in range(0, c)])
    r = all([h > G[r][x] for x in range(c + 1, cols)])
    if t or b or l or r:
        return True
    return False


ans = 0
for r in range(rows):
    for c in range(cols):
        if visible(r, c):
            ans += 1
print(ans)
