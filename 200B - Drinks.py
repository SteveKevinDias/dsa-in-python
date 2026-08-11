def drinks(n, p):
    total = 0
    for i in p:
        total += i
    return total / n


n = int(input())
p = list(map(int, input().split()))

print(drinks(n, p))
