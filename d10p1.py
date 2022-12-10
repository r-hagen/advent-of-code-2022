instructions = [line.strip() for line in open('d10input.txt').readlines()]

X = 1
C = 0
ans = 0

def signal():
    global ans
    x = [20, 60, 100, 140, 180, 220]
    if C in x:
        ans += C * X

for i in instructions:
    if i == 'noop':
        C += 1
        signal()
    else:
        _, val = i.split()
        val = int(val)
        C += 1
        signal()
        C += 1
        signal()
        X += val
print(ans)
