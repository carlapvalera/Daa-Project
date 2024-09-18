from Combinatoria import conjunto_potencia
from Chek import check

def monitorear_calle(n,bombillos,m):  
    if len(bombillos) == 0 or not check(n,bombillos,m):
        return -1
    best = len(bombillos)
    for conjunto in conjunto_potencia(len(bombillos)):
        postes = []
        for i in range(0,len(conjunto)):
            if conjunto[i] == 1:
                postes.append(bombillos[i])
        if len(postes) > 0 and check(n,postes,m) and len(postes) < best:
            best = len(postes)
    return best