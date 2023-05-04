inv = {}
fruta1={'fruta':'banana', 'preco': 2.0, 'quantidade': 1}
fruta2={'fruta':'macã', 'preco': 3.5, 'quantidade': 5}
fruta3={'fruta':'laranja', 'preco': 2.5, 'quantidade': 20}


inv['1']={'nome':'banana','preco': 2.0, 'quantidade': 1}
inv['2']={'nome':'macã', 'preco': 3.5, 'quantidade': 5}
print(inv)


num=int(input('Informe quantos produtos deseja cadastrar:' ))

for i in range(num):
    nome=input('Digite o nome do produto:' )
    preco=float(input('Digite o preco do produto:' ))
    quant=int(input('Digite a quantidade do produto:' ))
    inv[f'{i}']={'nome':nome, 'preco':preco, 'quantidade':quant}

print(inv['0']['preco'])