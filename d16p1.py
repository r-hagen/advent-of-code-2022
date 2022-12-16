import re

L = {}
DP = {}

for line in [line.strip() for line in open('d16.in').readlines()]:
    valve, rate, paths = re.search(r'Valve (\w{2}) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? (.*)', line).groups()
    rate = int(rate)
    paths = paths.split(', ')
    L[valve] = (rate, paths)

def f(pos, V, time):
    if time == 0:
        return 0

    key = (pos, tuple(sorted(V)), time)
    if key in DP:
        return DP[key]

    ans = 0

    if time > 0 and pos not in V and L[pos][0] > 0:
        new_V = set(V)
        new_V.add(pos)
        ans = max(ans, sum(L[o][0] for o in V) + f(pos, new_V, time - 1))

    if time > 0:
        for n in L[pos][1]:
            ans = max(ans, sum(L[o][0] for o in V) + f(n, V, time - 1))

    DP[key] = ans
    return ans

print(f('AA', set(), 30))
