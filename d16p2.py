import re

L = {}
DP = {}

for line in [line.strip() for line in open('d16.in').readlines()]:
    valve, rate, paths = re.search(r'Valve (\w{2}) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? (.*)', line).groups()
    rate = int(rate)
    paths = paths.split(', ')
    L[valve] = (rate, paths)

for k, v in L.items():
    s = sorted(v[1], key=lambda x: L[x][0], reverse=True)
    L[k] = (v[0], s)

def f(pos, V, time, elephant):
    if time == 0:
        if elephant:
            return f('AA', V, 26, False)
        else:
            return 0

    key = (pos, tuple(sorted(V)), time, elephant)
    if key in DP:
        return DP[key]

    ans = 0

    if pos not in V and L[pos][0] > 0:
        new_V = set(V)
        new_V.add(pos)
        ans = max(ans, (time-1)*L[pos][0] + f(pos, new_V, time-1, elephant))

    for n in L[pos][1]:
        ans = max(ans, f(n, V, time-1, elephant))

    DP[key] = ans

    return ans

print(f('AA', set(), 26, True))

