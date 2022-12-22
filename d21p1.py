from collections import deque

lines = [x.strip() for x in open('d21.in').readlines()]

M = {}
Q = deque([])

for line in lines:
    parts = line.split()
    if len(parts) == 2:
        M[parts[0][:-1]] = int(parts[1])
    elif len(parts) == 4:
        Q.append((parts[0][:-1], parts[1], parts[2], parts[3]))

while Q:
    m, n1, op, n2 = Q.popleft()
    if n1 in M and n2 in M:
        if op == '+':
            M[m] = M[n1] + M[n2]
        elif op == '-':
            M[m] = M[n1] - M[n2]
        elif op == '*':
            M[m] = M[n1] * M[n2]
        elif op == '/':
            M[m] = M[n1] / M[n2]
    else:
        Q.append((m, n1, op, n2))

print(M['root'])
