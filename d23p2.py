from collections import defaultdict

lines = [line.strip() for line in open('d23.in').readlines()]

G = {}
D = ['N', 'S', 'W', 'E']

# NW, N, NE, E, SE, S, SW, W, NW
NB = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1)]

def display():
    rmin = min([r for r, _ in G])
    rmax = max([r for r, _ in G])
    cmin = min([c for _, c in G])
    cmax = max([c for _, c in G])
    for r in range(rmin, rmax+1):
        for c in range(cmin, cmax+1):
            print('.' if (r, c) not in G or G[(r, c)] != '#' else '#', end='')
        print()
    print()

def iself(r, c):
    return (r, c) in G and G[(r, c)] == '#'

def elves():
    return [(r, c) for r, c in G if iself(r, c)]

def neighborelves(r, c):
    return [(r+rr, c+cc) for cc, rr in NB[:-1] if iself(r+rr, c+cc)]

def propose(r, c):
    for direction in D:
        if direction == 'N' and all(iself(r+rr, c+cc) == False for cc, rr in NB[0:3]):
            return ('N', (r-1, c))
        elif direction == 'S' and all(iself(r+rr, c+cc) == False for cc, rr in NB[4:7]):
            return ('S', (r+1, c))
        elif direction == 'W' and all(iself(r+rr, c+cc) == False for cc, rr in NB[6:9]):
            return ('W', (r, c-1))
        elif direction == 'E' and all(iself(r+rr, c+cc) == False for cc, rr in NB[2:5]):
            return ('E', (r, c+1))

for r in range(len(lines)):
    for c in range(len(lines[0])):
        G[(r, c)] = lines[r][c]
display()

round = 1
while True:
    proposals = defaultdict(list)
    GN = {}
    moved = len(elves())

    for r, c in elves(): 
        if len(neighborelves(r, c)) == 0: 
            proposals[(r, c)].append((r, c))
            moved -= 1
            continue

        proposal = propose(r, c)

        if proposal == None: 
            proposals[(r, c)].append((r, c))
            continue

        move_to = proposal[1]
        proposals[move_to].append((r, c))

    if moved == 0:
        print(round)
        break

    for move_to, move_from_ in proposals.items():
        if len(move_from_) > 1: 
            for elf in move_from_:
                GN[elf] = '#'
        else:
            GN[move_to] = '#'

    round += 1
    G = GN
    D.append(D.pop(0))

    # print('End of Round', round+1, moved)
    # display()
