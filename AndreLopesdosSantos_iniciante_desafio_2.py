from random import randint
print('PEDRA, PAPEL OU TESOURA')
itens = ('Pedra', 'Papel', 'Tesoura')

rodada = 0
pontosJogador = 0
pontosComputador = 0
nome = input('qual seu nome?\n')

while rodada < 5:
    print('Rodada n:{}'.format(rodada + 1))
    computador = randint(0, 2)
    jogador = input('Qual é a sua jogada?\n[0] Pedra\n[1] Papel\n[2] Tesoura\n')
    if not jogador.isdigit():
        print("Digite apenas os numeros 0, 1 ou 2 para realizar a sua jogada!")
        break
    jogador = int(jogador)
    if jogador > 2:
        print('jogada invalida, game over')
        break
    print("#" *30)
    print(' {} {} x ' .format(nome, itens[jogador]), end=' ')
    print('{} computador '.format(itens[computador]))
    if computador == 0: #pedra
        if jogador ==0:
            print('empate')
        elif jogador == 1:
            print('O {} venceu!' .format(nome))
            pontosJogador += 1
        elif jogador ==2:
            print('O computador venceu!')
            pontosComputador += 1
        else:
            print('jogada invalida')

    elif computador ==1: #papel
        if jogador == 0:
            print('O computador venceu!')
            pontosComputador += 1
        elif jogador == 1:
            print('empate')
        elif jogador == 2:
            print('O {} venceu!'.format(nome))
            pontosJogador += 1
        else:
            print('jogada invalida')

    elif computador == 2: #tesoura
        if jogador == 0:
            print('O {} venceu!'.format(nome))
            pontosJogador += 1
        elif jogador == 1:
            print('O computador venceu!')
            pontosComputador += 1
        elif jogador == 2:
            print('empate')
    else:
        print('jogada invalida')

    rodada += 1
    print("#" * 30)

    if rodada == 5:
        jogarNovamente = input('Deseja jogar novamente? S/N\n')
        if jogarNovamente[0] == 's' or jogarNovamente[0] == 'S':
            print('return')
            rodada = 0
        else:
            print('Jogador {} {} x {} Computador '.format(nome, pontosJogador, pontosComputador))