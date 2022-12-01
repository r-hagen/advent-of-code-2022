elves = open('d01input.txt', 'r').read().split('\n\n')
calories = [sum(map(int, snacks.strip().split('\n'))) for snacks in elves]
calories.sort(reverse=True)
print(sum(calories[:3]))
