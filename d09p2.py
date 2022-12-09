moves = [line.strip() for line in open('d09input.txt').readlines()]

H = (0, 0)
T = [(0, 0) for _ in range(9)]
DX = {"R": 1, "L": -1, "U": 0, "D": 0}
DY = {"R": 0, "L": 0, "U": 1, "D": -1}
TT = set()


def tail(H, T):
    dx = H[0] - T[0]
    dy = H[1] - T[1]
    if abs(dx) <= 1 and abs(dy) <= 1:
        pass
    elif abs(dx) >= 2 and abs(dy) >= 2:
        T = (H[0] - 1 if T[0] < H[0] else H[0] + 1, H[1] - 1 if T[1] < H[1] else H[1] + 1)
    elif abs(dx) >= 2:
        T = (H[0] - 1 if T[0] < H[0] else H[0] + 1, H[1])
    elif abs(dy) >= 2:
        T = (H[0], H[1] - 1 if T[1] < H[1] else H[1] + 1)
    return T


for move in moves:
    d, a = move.split()
    a = int(a)
    for _ in range(a):
        TT.add(T[-1])
        H = (H[0] + DX[d], H[1] + DY[d])
        T[0] = tail(H, T[0])
        for i in range(1, 9):
            T[i] = tail(T[i - 1], T[i])
        TT.add(T[-1])
print(len(TT))
