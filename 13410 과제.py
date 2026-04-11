n, k = map(int, input().split())
max_val = 0
for i in range(1, k + 1):
    rev_val = int(str(n * i)[::-1])
    if rev_val > max_val:
        max_val = rev_val
print(max_val)
