a = int(input())
b = int(input())

m = a+b
m = int(m/2)

if m>6:
    print('Aprovado')
elif m>3:
    print('Recuperação')
else:
    print('Reprovado')