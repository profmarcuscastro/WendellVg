n_pos = 0
n = 0
soma = 0
while n<6:
    n = n+1
    a = float(input())

    if a>0:
        n_pos = n_pos+1
        soma+=a
media =soma/n_pos
print(f'{n_pos} valores positivos')
print(f'{media:.1f}')



