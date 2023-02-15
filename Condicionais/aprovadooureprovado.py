a,b = map(float,input().split())
m = a+b
m = (m/2)

if m>=7:
    print('Aprovado')
elif m>=4:
    print('Recuperacao')
else:
    print('Reprovado')