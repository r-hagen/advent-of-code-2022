from collections import deque

numbers = list(map(int, open('d20.in').readlines()))
numbers = [x*811589153 for x in numbers]
Q = deque(list(enumerate(numbers)))

for _ in range(10):
    for i in range(len(Q)):
        while Q[0][0] != i:
            Q.append(Q.popleft())

        val = Q.popleft()
        pop = val[1]
        pop %= len(Q)

        for _  in range(pop):
            Q.append(Q.popleft())
        Q.append(val)

i = 0
while Q[i][1] != 0:
    i += 1

print(Q[(i+1000)%len(Q)][1] + Q[(i+2000)%len(Q)][1] + Q[(i+3000)%len(Q)][1])

