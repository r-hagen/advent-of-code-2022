from collections import deque

lines = [x.strip() for x in open('d21.in').readlines()]

M = {}
Q = deque([])
me = 'humn'

for line in lines:
    parts = line.split()
    if len(parts) == 2:
        m, n = parts
        m = m[:-1]
        if m == me:
            continue
        else:
            M[m] = int(n)
    elif len(parts) == 4:
        m, n1, op, n2 = parts
        m = m[:-1]
        if m == 'root':
            op = '='
        Q.append((m, n1, op, n2))

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
        elif op == '=':
            assert M[n1] == M[n2]
    elif op == '=' and (n1 in M or n2 in M):
        if n1 in M:
            M[n2] = M[n1]
        else:
            M[n1] = M[n2]
    elif m in M and n1 in M:
        if op == '+':
            M[n2] = M[m] - M[n1]
        elif op == '-':
            M[n2] = M[n1] - M[m]
        elif op == '*':
            M[n2] = M[m] / M[n1]
        elif op == '/':
            M[n2] = M[n1] / M[m]
    elif m in M and n2 in M:
        if op == '+':
            M[n1] = M[m] - M[n2]
        elif op == '-':
            M[n1] = M[m] + M[n2]
        elif op == '*':
            M[n1] = M[m] / M[n2]
        elif op == '/':
            M[n1] = M[m] * M[n2]
    else:
        Q.append((m, n1, op, n2))

print(M[me])
