numbers = [line.strip() for line in open('d25.in').readlines()]

def snafu_2_base10(snafu):
    S2D = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
    base10 = 0
    for i, d in enumerate(reversed(snafu)):
        base10 += pow(5, i) * S2D[d]
    return base10

def base10_2_snafu(base10):
    D2S = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}
    snafu = ''
    while base10 > 0:
        n = base10 % 5
        base10 //= 5
        if n in D2S:
            snafu = D2S[n] + snafu
            if n > 2: 
                base10 += 1
    return snafu

for number in numbers:
    base10 = snafu_2_base10(number)
    snafu = base10_2_snafu(base10)
    assert number == snafu, (number, base10, snafu)

sum = sum(map(snafu_2_base10, numbers))
print(base10_2_snafu(sum))
