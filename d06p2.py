signal = open('d06input.txt').readline()

ans = 0
for c in range(13, len(signal)):
    if len(set(signal[c-14:c])) == 14:
        ans = c
        break
print(ans)
