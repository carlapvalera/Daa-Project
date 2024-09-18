def check(n,postes,m):
    if postes[0] > m + 1 or n - postes[len(postes) - 1] > m:
        return False
    for i in range(0,len(postes) - 1):
        if postes[i + 1] - postes[i] > 2*m + 1:
            return False
    return True