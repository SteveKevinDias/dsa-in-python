def remove_duplicates(size, arr):
    hash = {}
    ans = []

    for i in range(size - 1, -1, -1):
        if arr[i] not in hash:
            hash[arr[i]] = 1
            ans.append(arr[i])

    ans.reverse()

    for i in range(len(ans)):
        arr[i] = ans[i]

    return len(ans)


n = int(input())
arr = list(map(int, input().split()))

k = remove_duplicates(n, arr)

print(k)
print(*arr[:k])
