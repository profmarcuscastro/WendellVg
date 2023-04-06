n1,n2,n3,n4 = map(float,input().split())

media  = n1*2+n2*3+n3*4+n4*1
media  = media/10

print(f'Media: {media:1f}')

if media >=7:
    print('Aluno aprovado.')
elif media<5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nota = float(input())
    print(f'Nota do exame: {nota}')
    media+=nota
    media=media/2
    if media >=5:
        print('Aluno aprovado.')
    else:
        print('Aluno Reprovado.')


    print(f'Media final: {media}')