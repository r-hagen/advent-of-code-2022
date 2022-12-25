from collections import defaultdict
import heapq

lines = [line.strip() for line in open('d24.in').readlines()]

rows = len(lines)
cols = len(lines[0])

MOVE = {'>': (1,0), '<': (-1,0), 'v': (0,1), '^': (0, -1)}
G = defaultdict(list)

for y in range(rows):
    for x in range(cols):
        if lines[y][x] != '.':
            G[(x,y)].append(lines[y][x])

def distance(E, F):
    return abs(E[0] - F[0]) + abs(E[1] - F[1])

def solve(S, F, G):
    pq = [(distance(S, F), 0, S, G)]
    tmin = 1_000_000
    gmin = G

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
                        for ch in G[(x,y)]:
                            if ch == '#':
                                GN[(x,y)].append(ch)
                            else:
                                gx = x + MOVE[ch][0]
                                gx = gx if gx > 0 else cols-2
                                gx = gx if gx < cols-1 else 1
                                gy = y + MOVE[ch][1]
                                gy = gy if gy > 0 else rows-2
                                gy = gy if gy < rows-1 else 1
                                GN[(gx,gy)].append(ch)
            GCACHE[t] = GN

        # advance elves
        ex, ey = E
        for e in [(ex,ey), (ex-1,ey), (ex+1,ey), (ex,ey-1), (ex,ey+1)]:
            if e == S or e == F or (0 < e[0] < cols and 0 < e[1] < rows and e not in GN):
                if e == F and t < tmin:
                    tmin = t
                    gmin = GN
                else:
                    heapq.heappush(pq, (distance(e, F), t, e, GN))

    return (tmin, gmin)


E = (1, 0)
F = (cols-2, rows-1)

t1, g1 = solve(E, F, G)
t2, g2 = solve(F, E, g1)
t3, g3 = solve(E, F, g2)

print(t1+t2+t3)
