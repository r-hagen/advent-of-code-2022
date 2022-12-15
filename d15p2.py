import re

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

S = set()
for line in [x.strip() for x in open('d15.in').readlines()]:
    sx, sy, bx, by = list(map(int, re.search(r'x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)', line).groups()))
    d = distance((sx,sy), (bx,by))
    S.add((sx,sy,d))

def beacon(x, y, S):
    for sx, sy, d in S:
        dd = distance((x,y), (sx,sy))
        if dd <= d:
            return False
    return True

for sx, sy, d in S:
    for dx in range(d):
        dy = (d+1) - dx
        for signx, signy in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:
            x = sx + (dx*signx)
            y = sy + (dy*signy)
            if not (0<=x<=4000000 and 0<=y<=4000000):
                continue
            assert distance((sx,sy), (x,y)) == d+1
            if beacon(x, y, S):
                print(x*4000000 + y)
                assert False

