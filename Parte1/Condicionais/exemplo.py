'''
Adulto maior ou igual a 20
Idoso maior ou igual a 60
Aborrecente menor do que 20

alto maior ou igual a 1.80
normal maior que 1.70 e menor que 1.80
baixo: menor que 1.70
'''

idade  =  int(input())
altura  = float(input())

if idade>= 20 and altura>180:
    print('a pessoa e adulta e alta')

if altura >= 180 or idade<20:
    print('ele e alto ou novo')

if not altura>180:
    print('ele nao e alto')