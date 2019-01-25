import random

lista =[]

#generator
for i in range(100):
    lista.append(random.randint(0,10))
    i+=1

print('Wygenerowano następujące liczby:')
print(lista)
print(len(lista))

#zliczacz ilości
for i in range(10):
    print('Wylosowano: ' + str(lista.count(i)) + ' elementów o numerze: ' + str(i))