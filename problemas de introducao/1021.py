n = float(input())

notas100 = n//100.00
n = n-100*notas100
notas50 = n//50.00
n = n-50*notas50
notas20 = n//20.00
n = n-20*notas20
notas10 = n//10.00
n = n-10*notas10
notas5 = n//5.00
n = n-5*notas5
notas2 = n//2.00
n = n-2*notas2
moedas100 = n//1.00
n = n-1.00*moedas100
moedas50 = n//0.50
n = n-0.50*moedas50
moedas25 = n//0.25
n = n-0.25*moedas25
moedas10 = n//0.10
n = n-0.10*moedas10
moedas5 = n//0.05   
n = n-0.05*moedas5
moedas1 = n//0.01
if moedas1 >0:
    moedas1+=1

print('NOTAS:')
print(int(notas100),'nota(s) de R$ 100.00')
print(int(notas50),'nota(s) de R$ 50.00')
print(int(notas20), 'nota(s) de R$ 20.00')
print(int(notas10), 'nota(s) de R$ 10.00')
print(int(notas5 ),'nota(s) de R$ 5.00')
print(int(notas2 ),'nota(s) de R$ 2.00')
print('MOEDAS:')
print(int(moedas100), 'moeda(s) de R$ 1.00')
print(int(moedas50), 'moeda(s) de R$ 0.50')
print(int(moedas25), 'moeda(s) de R$ 0.25')
print(int(moedas10), 'moeda(s) de R$ 0.10')
print(int(moedas5),'moeda(s) de R$ 0.05')
print(int(moedas1),'moeda(s) de R$ 0.01')