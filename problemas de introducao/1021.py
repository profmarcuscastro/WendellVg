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
n = n-5*notas10
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
n = n-0.01*moedas1

print('NOTAS:')
print(notas100,'nota(s) de R$ 100.00')
print(notas50,'nota(s) de R$ 50.00')
print(notas20, 'nota(s) de R$ 20.00')
print(notas10, 'nota(s) de R$ 10.00')
print(notas5, 'nota(s) de R$ 5.00')
print(notas2, 'nota(s) de R$ 2.00')
print('MOEDAS:')
print(moedas100, 'moedas(s) de R$ 1.00')
print(moedas50, 'moedas(s) de R$ 0.50')
print(moedas25, 'moedas(s) de R$ 0.25')
print(moedas10, 'moedas(s) de R$ 0.10')
print(moedas5, 'moedas(s) de R$ 0.05')
print(moedas1, 'moedas(s) de R$ 0.01')