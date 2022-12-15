import re

ans = 0
n = 2000000

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

S = set()
for line in [x.strip() for x in open('d15.in').readlines()]:
    sx, sy, bx, by = list(map(int, re.search(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line).groups()))
    S.add((sx,sy,bx,by))

G = {}
for sx, sy, bx, by in S:
    G[(sx, sy)] = 'S'
    G[(bx, by)] = 'B'
    if sy == n:
        ans += 1

for sx, sy, bx, by in S:
    d = distance((sx,sy), (bx,by))
    dy = abs(n - sy)
    if dy <= d:
        k = 2*d - (dy*2)
        for x in range(sx-k//2, sx+k//2+1):
            if distance((sx,sy), (x,n)) <= d:
                if (x, n) not in G:
                    G[(x, n)] = '#'
                    ans += 1
print(ans)

