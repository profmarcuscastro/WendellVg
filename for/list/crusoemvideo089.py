lista_alunos=[]


while True:
    print('Quer continuar? S/N')

    #input() sempre recebe dados no formato de string
    comp= input()
    #if CONDICAO: (SE COND VERDADEIRA VAI RODAR OQ ESTA DENTRO DO IF)
    if comp=='N':
        break

    nome = input()
    nota1 = float(input())
    nota2 = float(input())
    media = nota1+nota2
    media =media/2
    lista_alunos.append([nome,[nota1,nota2],media])

for aluno in lista_alunos:
    print(f'nome: {aluno[0]}')
    print(f'media: {aluno[2]}')