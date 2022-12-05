import re

top, bottom = open('d05input.txt').read().split('\n\n')

stacks = [[] for _ in range(0, 9)]
for line in top.split('\n'):
    si = 0
    for li in range(1, 9 * 4, 4):
        if line[li].isalpha():
            stacks[si].insert(0, line[li])
        si += 1

instructions = []
for line in bottom.split('\n'):
    a, f, t = map(int, re.search('move (\d+) from (\d+) to (\d+)', line).groups())
    instructions.append((a, f, t))

for a, f, t in instructions:
    crates = []
    for i in range(a):
        crates.append(stacks[f - 1].pop())
    for crate in crates[::-1]:
        stacks[t - 1].append(crate)

print(''.join([x.pop() for x in stacks]))
