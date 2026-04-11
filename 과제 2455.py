max_p = 0
curr_p = 0
for _ in range(4):
    out_p, in_p = map(int, input().split())
    curr_p += in_p - out_p
    if curr_p > max_p:
        max_p = curr_p
print(max_p)
