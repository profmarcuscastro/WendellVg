lados = list(map(float,input().split()))
a,b,c = lados
lados.sort()

if lados[2]<lados[1]+lados[0]:
    perimetro = sum(lados)
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = (a+b)*c
    area /=2
    print(f'Area = {area:.1f}')