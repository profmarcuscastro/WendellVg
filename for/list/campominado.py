n = int(input())
campo = []
lista = []
for i in range(n):
    a = int(input())
    campo.append(a)
    #print(campo)

for i in range(len(campo)):
    cont = 0
    if campo[i]==1:
        cont +=1
    if i != n-1:
        if campo[i+1]==1:
            cont+=1
    if i!=0:
        if campo[i-1]==1:
            cont+=1
    lista.append(cont)

for i in range(len(lista)):
    print(lista[i])