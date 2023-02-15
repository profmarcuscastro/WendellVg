neg = 0
pos = 0
imp = 0
par = 0
a = 0
while a<5:
    a = a+1
    n = int(input())
    if n%2==0:
        par = par+1
    else:
        imp = imp+1
    
    if n>0:
        pos = pos+1
    elif n<0:
        neg = neg+1

print(f'{par} valor(es) par(es)')
print(f'{imp} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')