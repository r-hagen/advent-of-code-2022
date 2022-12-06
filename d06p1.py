signal = open('d06input.txt').readline()

ans = 0
for c in range(3, len(signal)):
    if len(set(signal[c-4:c])) == 4:
        ans = c
        break
print(ans)
