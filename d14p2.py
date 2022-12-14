G = {}
for x in open('d14.in').readlines():
    path = [list(map(int, y.split(','))) for y in x.strip().split(' -> ')]
    f = path.pop(0)
    while len(path) > 0:
        t = path.pop(0)

        if f[0] < t[0]:
            dx = [f[0]+x for x in range(abs(f[0]-t[0])+1)]
        else:
            dx = [f[0]-x for x in range(abs(f[0]-t[0])+1)]

        if f[1] < t[1]:
            dy = [f[1]+x for x in range(abs(f[1]-t[1])+1)]
        else:
            dy = [f[1]-x for x in range(abs(f[1]-t[1])+1)]

        for y in dy:
            for x in dx:
                G[(x,y)] = '#'
        f = t

xmin = min(G.keys(), key=lambda t: t[0])[0]
xmax = max(G.keys(), key=lambda t: t[0])[0]
ymin = min(G.keys(), key=lambda t: t[1])[1]
ymax = max(G.keys(), key=lambda t: t[1])[1]

for x in range(xmin-10000, xmax+10000):
    G[(x, ymax+2)] =  '#'
ymax += 2

def pg(s=None):
    for y in range(ymin-5, ymax+1):
        for x in range(xmin-5, xmax+6):
            if s and s == (x, y):
                print('+', end='')
            elif (x, y) in G:
                print(G[(x, y)], end='')
            else:
                print('.', end='')
        print()

S = (500, 0)
ans = 0
while True:
    x, y = S
    if (x, y+1) not in G:
        S = (x, y+1)
    elif (x-1, y+1) not in G:
        S = (x-1, y+1)
    elif (x+1, y+1) not in G:
        S = (x+1, y+1)
    else:
        ans += 1
        if S == (500, 0):
            break
        G[S] = '+'
        S = (500, 0)

    # if ans % 1000 == 0:
    #     pg(S)

print(ans)
