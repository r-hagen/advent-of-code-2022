import re

blocks = [monkey.splitlines() for monkey in open('d11.in').read().split('\n\n')]
monkeys = [[] for _ in range(len(blocks))]

for b in blocks:
    idx = int(re.search('^Monkey (\d*):', b[0]).groups()[0])
    items = list(map(int, re.search('Starting items: (.*)', b[1]).groups()[0].split(',')))
    op = re.search('Operation: new = (.*)', b[2]).groups()[0]
    test = int(re.search('Test: divisible by (\d*)', b[3]).groups()[0])
    true = int(re.search('If true: throw to monkey (\d*)', b[4]).groups()[0])
    false = int(re.search('If false: throw to monkey (\d*)', b[5]).groups()[0])
    monkeys[idx] = [items, op, test, true, false]

lcm = 1
for m in monkeys:
    lcm *= m[2]

ans = [0 for _ in range(len(blocks))]
for _ in range(10000):
    for mi, m in enumerate(monkeys):
        i = 0
        while len(m[0]) > 0:
            ans[mi] += 1
            old = m[0].pop(0)
            worry = eval(m[1])
            worry %= lcm
            if worry % m[2] == 0:
                monkeys[m[3]][0].append(worry)
            else:
                monkeys[m[4]][0].append(worry)

ans.sort(reverse=True)
print(ans[0]*ans[1])

