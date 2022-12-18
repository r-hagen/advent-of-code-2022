from collections import deque

cubes = [tuple(map(int, line.split(','))) for line in open('d18.in').readlines()]


def neighbors(cube):
    x,y,z = cube
    nb = set()
    nb |= set((x,y,z) for z in [z-1, z+1])
    nb |= set((x,y,z) for y in [y-1, y+1])
    nb |= set((x,y,z) for x in [x-1, x+1])
    return nb


xmin = min(x for x,_,_ in cubes)
xmax = max(x for x,_,_ in cubes)
ymin = min(y for _,y,_ in cubes)
ymax = max(y for _,y,_ in cubes)
zmin = min(z for _,_,z in cubes)
zmax = max(z for _,_,z in cubes)
print(zmin, zmax)


box = set()
for z in range(zmin-3, zmax+3):
    for y in range(ymin-3, ymax+3):
        for x in range(xmin-3, xmax+3):
            box.add((x,y,z))
box = list(box)

V = set()
V.add(box[0])
Q = deque([box[0]])

while Q:
    p = Q.popleft()
    for n in neighbors(p):
        if (n not in cubes) and (n not in V) and (n in box):
            Q.append(n)
            V.add(n)

ans = 0
for c in cubes:
    nb = neighbors(c)
    ans += sum(n in V for n in nb)
print(ans)
