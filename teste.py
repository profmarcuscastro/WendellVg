mdeidade = []
nomes = []
idades = []
alturas = []
n = int(input())
while n>0:
    n-=1
    nome = input('insira um nome: ')
    idade = int(input('insira uma idade: '))
    altura = float(input('insira uma altura: '))
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)

for i in range(len(nomes)):
    if idades[i]>=18:
        mdeidade.append(nomes[i])
print(f'os maiores de idade são: ')

for elemento in mdeidade:
    print(elemento)

