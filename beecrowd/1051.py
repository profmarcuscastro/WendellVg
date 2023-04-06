x = float(input())

if 0<=x<2000:
    print(f'Isento')
elif 2000<=x<=3000:
    print(f'R$ {x*8/100:.2f}')
elif 3000<x<=4500:
    print(f'R$ {x*18/100:.2f}')
else :
    print(f'R$ {x*28/100:.2f}')