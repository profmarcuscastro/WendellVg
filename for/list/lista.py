#index   0,1,2,3,4,5,6
lista = [1,2,3,4,5,6,7]

for i in range(2,len(lista)):
    print(lista[i])
    if lista[i]==5:
        lista[i+1]='WENDELL'

for elemento in lista:
    print(elemento)