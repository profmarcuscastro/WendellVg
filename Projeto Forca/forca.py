import time 

print('Jogo da Forca')
palavra_chave = input('Insira a palavra: ')
vidas = int(input('Escolha qual a quantidade de erros: '))
print('Processando palavra...\n')

time.sleep(2) 

print(f'A palavra a ser acertada e {palavra_chave}')
print(f'Voce tem {vidas} vidas para isso')

time.sleep(2)

print('.\n'*100)
'''
String possui comandos de lista 

len(lista)--> Retorna o tamanho de uma lista
len(str)--> Retorna o tamanho de uma string
'''

aux =  '*'*len(palavra_chave)

print(f'Palavra a ser adivinhada: {aux}')

time.sleep(5)

print(f'\n {"#"*15}JOGO INICIADO!!{"#"*15} \n')
'''
Definindo Processos do jogo

input da letra tentada
Verificar se na palavra possui a letra escolhida
caso verdade: substituir a letra no lugar do asterisco 
verificar se palavra chave == palavra atual 

caso nao: diminuir uma vida
    verificar se ainda possui vidas
        caso nao: avisar que perdeu o jogo
'''
acertadas = []
digitas = []
while True:
    letra_tentada=input('Tente uma letra: ')
    
    
    if letra_tentada in digitas:
        print('Tente outra letra. Essa ja foi tentada.\n\n')
        continue
    digitas.append(letra_tentada)

    if letra_tentada in palavra_chave:
        acertadas.append(letra_tentada)
        aux = ""
        for letra in palavra_chave:
            aux+= letra if letra in acertadas else '*'

        if not '*' in aux:
            print(f'Parabens!!! Voce ganhou o jogo com {vidas} vidas restantes')
            break
        print(f'Estado atual: {aux}')
        

    else:
        vidas=vidas-1
        print(f'A letra {letra_tentada} nao esta na palavra. Voce tem {vidas} vidas')
        if vidas==0:
            print('Suas vidas acabaram. Voce perdeu o jogo!!!')
            break

print('FIM DE JOGO!!!')