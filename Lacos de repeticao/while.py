'''
x=int(input())
while x>0:
    x = x-1
    nome = input('Insira um nome:')
    idade= int(input('Insira uma idade em anos: '))

    if idade>18:
        print(f'A pessoa: {nome} é maior de idade')
    if idade==30:
        break
    else: 
        print(f'A pessoa: {nome} é menor de idade')
print('saiu')

'''
i = 0
while True:
    i = i+1
    print(i)
    x = int(input())
    if x==3:
        break
