assignments = [line.strip().split(',') for line in open('d04input.txt', 'r').readlines()]
ans = 0
for pair in assignments:
    (start1, end1) = map(int, pair[0].strip().split('-'))
    (start2, end2) = map(int, pair[1].strip().split('-'))
    if start1 <= end2 and start2 <= end1:
        ans += 1
print(ans)
