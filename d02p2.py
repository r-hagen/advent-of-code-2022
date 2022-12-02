rounds = [line.strip().split(' ') for line in open('d02input.txt', 'r').readlines()]
rules = {
    ('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8,
    ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
    ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7,
}
print(sum([rules[(a, b)] for a, b in rounds]))
