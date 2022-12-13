lines = [line.strip() for line in open('d13.in').readlines() if line.strip()]

def listify(s):
    l = []
    i = 0
    while i < len(s):
        # parse number
        n = []
        while i < len(s) and s[i].isnumeric():
            n.append(s[i])
            i += 1
        if len(n) > 0:
            l.append(int(''.join(n)))
        # parse list
        if i < len(s) and s[i] == '[' and i != 0:
            o, c, k = 1, 0, i+1
            while k < len(s):
                if s[k] == '[':
                    o += 1
                elif s[k] == ']':
                    c += 1
                if o == c:
                    break
                k += 1
            l.append(listify(s[i:k+1]))
            i += k - i + 1
        i += 1
    if len(l) == 1 and not s.startswith('['):
        return l[0]
    return l

def check(ll, rr):
    # valid = 1 invalid = 2 continue = 3
    for i in range(len(ll)):
        if not i < len(rr):
            print('right side ran out of items, so inputs are not in the right order')
            return 2
        left, right = ll[i], rr[i]
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                print('left side is smaller, so inputs are in the right order')
                return 1
            elif left > right:
                print('right side is smaller, so inputs are not in the right order')
                return 2
        elif isinstance(left, list) and isinstance(right, list):
            valid = check(left, right)
            if valid != 3:
                return valid
        else:
            if isinstance(left, int):
                valid = check([left], right)
                if valid != 3:
                    return valid
            else:
                valid = check(left, [right])
                if valid != 3:
                    return valid
    if len(ll) < len(rr):
        print('left side ran out of items, so inputs are in the right order')
        return 1
    return 3

lines = lines + ['[[2]]', '[[6]]']

while True:
    swapped = False
    for i in range(len(lines)-1):
        left, right = lines[i], lines[i+1]
        res = check(listify(left), listify(right))
        if res == 2:
            t = left
            lines[i] = right
            lines[i+1] = left
            swapped = True
    if not swapped:
        break

i1 = lines.index('[[2]]') + 1
i2 = lines.index('[[6]]') + 1

print(i1*i2)
