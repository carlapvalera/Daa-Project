MAXN = 100010

def solve():
    global n, a, pos, nxt
    
    n = int(input())
    a = [0] + list(map(int, input().split()))
    pos = [n + 1] * (n + 1)
    nxt = [0] * (n + 1)
    
    for i in range(n, -1, -1):
        nxt[i] = pos[a[i]]
        pos[a[i]] = i
    
    x, y = 0, 0  # the last elements of the two subarrays
    res = 0
    
    for z in range(1, n + 1):
        # Greedy Strategy I
        if a[x] == a[z]:
            res += a[y] != a[z]
            y = z
        elif a[y] == a[z]:
            res += a[x] != a[z]
            x = z
        # Greedy Strategy II
        elif nxt[x] < nxt[y]:
            res += a[x] != a[z]
            x = z
        else:
            res += a[y] != a[z]
            y = z
    
    print(res)

solve()