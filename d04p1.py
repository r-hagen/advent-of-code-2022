assignments = [line.strip().split(',') for line in open('d04input.txt', 'r').readlines()]
ans = 0
for pair in assignments:
    (start1, end1) = map(int, pair[0].strip().split('-'))
    (start2, end2) = map(int, pair[1].strip().split('-'))
    if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
        ans += 1
print(ans)
