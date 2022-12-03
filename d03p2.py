rucksacks = [line.strip() for line in open('d03input.txt', 'r').readlines()]
sum = 0
for i in range(0, len(rucksacks), 3):
    g = rucksacks[i:i + 3]
    for b in g[0]:
        if b in g[1] and b in g[2]:
            sum += ord(b) - 96 if b.islower() else ord(b) - 38
            break
print(sum)
