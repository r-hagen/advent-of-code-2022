from collections import defaultdict
import heapq

lines = [line.strip() for line in open('d24.in').readlines()]

rows = len(lines)
cols = len(lines[0])

M = {'>': (1,0), '<': (-1,0), 'v': (0,1), '^': (0, -1)}
G = defaultdict(list)

S = E = (1, 0)
F = (cols-2, rows-1)

for y in range(rows):
    for x in range(cols):
        if lines[y][x] != '.':
            G[(x,y)].append(lines[y][x])

def distance(E, F):
    return abs(E[0] - F[0]) + abs(E[1] - F[1])

pq = [(distance(E, F), 0, E, G)]
tmin = 1_000_000

SEEN = set()
GCACHE = {}

while True:
    if len(pq) == 0: break
    d, t, E, G = heapq.heappop(pq)

    if t > tmin: continue
    if d > (tmin-t): continue
    if (t, E) in SEEN: continue
    SEEN.add((t, E))

    GN = defaultdict(list)
    t += 1

    # advance blizzards
    if t in GCACHE:
        GN = GCACHE[t]
    else:
        for y in range(rows):
            for x in range(cols):
                if (x,y) in G:
                    for g in G[(x,y)]:
                        if g == '#':
                            GN[(x,y)].append(g)
                        else:
                            gx = x + M[g][0]
                            gx = gx if gx > 0 else cols-2
                            gx = gx if gx < cols-1 else 1
                            gy = y + M[g][1]
                            gy = gy if gy > 0 else rows-2
                            gy = gy if gy < rows-1 else 1
                            GN[(gx,gy)].append(g)
        GCACHE[t] = GN

    # advance elves
    ex, ey = E
    for e in [(ex,ey), (ex-1,ey), (ex+1,ey), (ex,ey-1), (ex,ey+1)]:
        if e == S or (0 <e [0] < cols and 0 <e[1] < rows and e not in GN):
            if e == F and t < tmin:
                tmin = t
            heapq.heappush(pq, (distance(e, F), t, e, GN))

print(tmin)
