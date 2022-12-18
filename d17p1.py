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
    if len(C) == 0:
        return 0
    return max(C, key=lambda t: t[1])[1]


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
    global R
    sy = hrock(C) + 4
    return [(x+2, y+sy) for x, y in R[ri]]


C = set()
stopped = 0

FALL = 0
JET = 1
m = JET

r = spawn(C, 0)
ri = 1
ji = 0

while stopped < 2022:
    if m == FALL:
        rn = [(x, y-1) for x, y in r]
        if bcollide(C, rn):
            C.update(r)
            r = spawn(C, ri)
            ri = ri+1 if ri+1 < len(R) else 0
            stopped += 1
        else:
            r = rn
        m = JET
    else:
        if J[ji] == '<':
            rn = [(x-1, y) for x, y in r]
            if not wcollide(C, rn):
                r = rn
        elif J[ji] == '>':
            rn = [(x+1, y) for x, y in r]
            if not wcollide(C, rn):
                r = rn
        ji = ji+1 if ji+1 < len(J) else 0
        m = FALL

print(hrock(C))
