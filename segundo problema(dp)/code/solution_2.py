from Chek import check

def solution_2(n,postes,m):
    if len(postes) == 0 or not check(n,postes,m):
        return -1
    last = 0
    dp = [0] * (n + 1)
    for i in range(0,len(postes)):
        temp = 1
        if postes[i] - m - 1 >= 0:
            temp = dp[postes[i] - m - 1] + 1
        for j in range(max(last + 1,postes[i] - m),min(postes[i] + m, n)+1):
            dp[j] = temp
        last = min(postes[i] + m,n)
    return dp[n]