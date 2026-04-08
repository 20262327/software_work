a = []
[a.pop() if (b := int(input())) == 0 else a.append(b) for _ in range(int(input()))]
print(sum(a))