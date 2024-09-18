from random import *
from Combinatoria import conjunto_potencia
from Fuerza_Bruta import monitorear_calle
from solution_1 import solution_1
from solution_2 import solution_2
from solution_3 import solution_3

min_calle = 50
max_calle = 100
solutions = [monitorear_calle,solution_1,solution_2,solution_3]
max_bombillo = max_calle

def tester(min_calle,max_calle,max_bombillo,solutions):
    if len(solutions) == 0:
        print("ERROR: Not solutions")
        return
    count = 0
    good = True
    for n in range(min_calle,max_calle):
        for conj in conjunto_potencia(n):
            postes = []
            for j in range(0,n):
                if conj[j] == 1:
                    postes += [j + 1]
            if len(postes) == 0:
                continue
            for m in range(1,max_bombillo + 1):
                # count += 1
                # print("Test:",count)
                ls =[]
                s_real = solutions[0](n,postes,m)
                ls.append(s_real)
                for i in range(1,len(solutions)):
                    s = solutions[i](n,postes,m)
                    ls.append(s)
                    if s != s_real:
                        print("Solution ",i,": ",n,postes,m)
                        return
                print(ls)

def tester(min_calle,max_calle,solutions):
    count = 0
    while True:
        count += 1
        calle = randint(min_calle,max_calle)
        population = [i for i in range(1,calle + 1)]
        postes = sorted(sample(population,min(randint(1,calle),10)))
        intensidad = randint(1,int(calle/2))
        print("Test ",count,":",calle,postes,intensidad)
        ls = []
        ls.append(solutions[0](calle,postes,intensidad))
        for sol in range(1,len(solutions)):
            value = solutions[sol](calle,postes,intensidad)
            assert value == ls[0]
            ls.append(value)
        print("     ",ls[0])

tester(min_calle,max_calle,solutions)