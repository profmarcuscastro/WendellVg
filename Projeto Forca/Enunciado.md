# Problema da forca 

## Funcionalidades

### Input
    - escolha da palavra a ser adivinhada 
    - quantidade de erros que esta permitido a ter 

### OUTPUT: a cada rodada

    exibir como a palavra esta atualmente 
    quais letras ja foram tentantadas
    quantidade de vidas pendentes

### Observacoes

    - Programa de verificar se a letra ja foi tentado ou nao de dar uma resposta coerente a isso
    - mostrar quando o jogo foi ganho ou perdido


Segue uma sugestão de detalhamento das mensagens de saída do jogo:

Ao iniciar o jogo, o programa deve exibir a mensagem "Jogo da forca" e solicitar que o usuário insira a palavra a ser adivinhada. Exemplo: "Insira a palavra: ".

Após o usuário inserir a palavra, o programa deve "limpar" a tela e exibir uma mensagem de espera de alguns segundos, para dar a impressão de que o programa está pensando em uma palavra. Exemplo: "Processando a palavra...".

Em seguida, o programa deve exibir a quantidade de letras da palavra, substituindo cada letra por um asterisco (*). Exemplo: "A palavra tem 5 letras: *****".

O programa deve então entrar em um loop que irá continuar enquanto o usuário ainda tiver chances de acertar a palavra. A cada iteração do loop, o programa deve solicitar que o usuário digite uma letra.

Se o usuário digitar mais de uma letra, o programa deve exibir a mensagem "Digite apenas uma letra". Exemplo: "Digite a letra: ab".

Se o usuário digitar uma letra que já foi digitada anteriormente, o programa deve exibir a mensagem "A letra <letra> já foi inserida". Exemplo: "Digite a letra: a. A letra a já foi inserida".

Se o usuário digitar uma letra que faz parte da palavra, o programa deve exibir a mensagem "A letra <letra> está na palavra" e exibir a palavra com as letras já adivinhadas preenchidas. Exemplo: "Digite a letra: o. A letra o está na palavra: o**".

Se o usuário digitar uma letra que não faz parte da palavra, o programa deve exibir a mensagem "A letra <letra> não está na palavra" e diminuir em 1 as chances restantes. Exemplo: "Digite a letra: z. A letra z não está na palavra. Você tem 5 chances restantes".

O programa deve continuar solicitando que o usuário digite letras até que ele acerte todas as letras da palavra ou as chances acabem.

Ao final do jogo, o programa deve exibir a mensagem "Você ganhou" caso o usuário tenha acertado todas as letras da palavra e exibir a mensagem "Você perdeu" caso o usuário tenha acabado com todas as chances sem adivinhar a palavra. O programa também deve exibir a palavra correta. Exemplo: "Você ganhou! A palavra era ABACAXI".