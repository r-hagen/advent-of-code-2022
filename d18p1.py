from collections import defaultdict

cubes = [tuple(map(int, line.split(','))) for line in open('d18.in').readlines()]
C = defaultdict(set)

for cx, cy, cz in cubes:
    C[(cx,cy,cz)] |= set((cx,cy,z) for z in [cz-1, cz+1] if (cx,cy,z) in cubes)
    C[(cx,cy,cz)] |= set((cx,y,cz) for y in [cy-1, cy+1] if (cx,y,cz) in cubes)
    C[(cx,cy,cz)] |= set((x,cy,cz) for x in [cx-1, cx+1] if (x,cy,cz) in cubes)

print(sum(6-len(v) for v in C.values()))
