rucksacks = [line.strip() for line in open('d03input.txt', 'r').readlines()]
sum = 0
for r in rucksacks:
    half = len(r) // 2
    c1, c2 = r[:half], r[half:]
    for i in c1:
        if i in c2:
            sum += ord(i) - 96 if i.islower() else ord(i) - 38
            break
print(sum)
