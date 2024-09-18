from Chek import check

def solution_3(n,postes,m):
    if not check(n,postes,m):
        return -1
    A = [0]*(len(postes)+1)
    A[1] = min(n,postes[0] + m)
    current = 1
    if A[1] == n:
        return 1
    for i in range(1,len(postes)):
        if A[max(0,current - 1)] < postes[i] - m - 1:
            current += 1
        A[current] = min(n,postes[i] + m)
        if A[current] == n:
            return current
    return -1