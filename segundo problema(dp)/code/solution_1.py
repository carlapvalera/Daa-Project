from Chek import check

def solution_1(n,postes,m):
    if len(postes) == 0 or not check(n,postes,m):
        return -1
    dp = [0] * (n + 1)
    for i in range(0,len(postes)):
        temp = 1
        if postes[i] - m - 1 >= 0:
            temp = dp[postes[i] - m - 1] + 1
        for j in range(max(1,postes[i] - m),min(postes[i] + m, n) + 1):
            if dp[j] == 0:
                dp[j] = temp
    return dp[n]