from collections import deque

numbers = list(map(int, open('d20.in').readlines()))
Q = deque(list(enumerate(numbers)))

for i in range(len(Q)):
    while Q[0][0] != i:
        Q.append(Q.popleft())

    val = Q.popleft()
    pop = val[1]

    if pop > 0:
        for _  in range(pop):
            Q.append(Q.popleft())
        Q.append(val)
    else:
        for _ in range(abs(pop)):
            Q.appendleft(Q.pop())
        Q.appendleft(val)

while Q[0][1] != 0:
    Q.append(Q.popleft())

print(Q[1000%len(Q)][1] + Q[2000%len(Q)][1] + Q[3000%len(Q)][1])

