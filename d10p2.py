instructions = [line.strip() for line in open('d10input.txt').readlines()]

X = 1
C = 0
CRT = [['.'] * 40 for _ in range(6)]

def signal():
    rr = [40, 80, 120, 160, 200, 240]
    ri = -1
    ci = -1
    for x in rr:
        if C <= x:
            ri = rr.index(x)
            ci = C - 1 - ri * 40
            break

    if ci in [X-1, X, X+1]:
        CRT[ri][ci] = '#'

for i in instructions:
    if i == 'noop':
        C += 1
        signal()
    else:
        _, val = i.split()
        val = int(val)
        C += 1
        signal()
        C += 1
        signal()
        X += val

for y in range(6):
    for x in range(40):
        print(CRT[y][x], end='')
    print()
