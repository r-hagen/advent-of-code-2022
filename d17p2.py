J = list(open('d17.in').read().strip())

r0 = [
        (0,0),(1,0),(2,0),(3,0)
]
r1 = [
              (1,2),
        (0,1),(1,1),(2,1),
              (1,0)
]
r2 = [
                    (2,2),
                    (2,1),
        (0,0),(1,0),(2,0)
]
r3 = [
        (0,3),
        (0,2),
        (0,1),
        (0,0)
]
r4 = [
        (0,1),(1,1),
        (0,0),(1,0)
]
R = [r0, r1, r2, r3, r4]


def hrock(C):
    return max([y for x, y in C])


def bcollide(C, r):
    for x, y in r:
        if (x, y) in C or y == 0:
            return True
    return False


def wcollide(C, r):
    for x, y in r:
        if (x, y) in C or x < 0 or x >= 7:
            return True
    return False


def spawn(C, ri):
    sy = hrock(C) + 4
    return [(x+2, y+sy) for x, y in R[ri]]


def signature(C):
    ymax = hrock(C)
    return frozenset([(x, ymax-y) for x, y in C if ymax-y <= 30])


C = set([(x, 0) for x in range(7)])
N = 1000000000000

s = 0
top = 0
added = 0

rock = spawn(C, 0)
ri = 0
ji = 0

SEEN = {}

while s < N:
    rock = spawn(C, s % len(R))
    while True:
        if J[ji] == '<':
            rn = [(x-1, y) for x, y in rock]
            if not wcollide(C, rn):
                rock = rn
        elif J[ji] == '>':
            rn = [(x+1, y) for x, y in rock]
            if not wcollide(C, rn):
                rock = rn
        ji = (ji+1) % len(J)

        rn = [(x, y-1) for x, y in rock]
        if bcollide(C, rn):
            C.update(rock)
            top = hrock(C)

            SR = (ji, s % 5, signature(C))
            if SR in SEEN:
                olds, oldt = SEEN[SR]
                dy = top - oldt
                ds = s - olds
                amt = (N-s)//ds
                added += amt*dy
                s += amt*ds
                assert s <= N
            SEEN[SR] = (s, top)
            break
        else:
            rock = rn
    s += 1

print(top+added)
