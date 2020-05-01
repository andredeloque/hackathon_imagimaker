print('Calculadora de Minimo Múltiplo Comum M.M.C e Máximo Multiplo Comum M.M.D')
print('Digite cinco números inteiros')

while True:
    numero1 = input('Digite o primeiro número\n')
    numero2 = input('Digite o segundo número\n')
    numero3 = input('Digite o terceiro número\n')
    numero4 = input('Digite o quarto número\n')
    numero5 = input('Digite o quinto número\n')

    erro = 'Não é possivel calcular o m.m.c e m.d.c com os números fornecidos'
    if not numero1.isdigit():
        print(erro)
        break
    else:
        numero1 = int(numero1)

    if not numero2.isdigit():
        print(erro)
        break
    else:
        numero2 = int(numero2)

    if not numero3.isdigit():
        print(erro)
        break
    else:
        numero3 = int(numero3)

    if not numero4.isdigit():
        print(erro)
        break
    else:
        numero4 = int(numero4)

    if not numero5.isdigit():
        print(erro)
        break
    else:
        numero5 = int(numero5)

    if (numero1 > 1000 or
            numero2 > 1000 or
            numero3 > 1000 or
            numero4 > 1000 or
            numero5 > 1000):
        print('Meu programa não é  obrigado a calcular isso.')
        break

    num = (numero1, numero2, numero3, numero4, numero5)
    posicao = 0
    primo = False
    while posicao < 5:
        total = 0
        for c in range(1, num[posicao] + 1):
            if num[posicao] % c == 0:
                total += 1
        if total == 2:
            print('o numero {} é Primo'.format(num[posicao]))
            primo = True
        posicao += 1
        if posicao == 4:
            if primo == False:
                print('Nenhum número lido é primo')

    maior = numero1
    if numero2 > numero1 and numero2 > numero3 and numero2 > numero4 and numero2 > numero5:
        maior = numero2
    if numero3 > numero1 and numero3 > numero2 and numero3 > numero4 and numero3 > numero5:
        maior = numero3
    if numero4 > numero1 and numero4 > numero2 and numero4 > numero3 and numero4 > numero5:
        maior = numero4
    if numero5 > numero1 and numero5 > numero2 and numero5 > numero3 and numero5 > numero4:
        maior = numero5

    while True:
        if maior % numero1 == 0 and maior % numero2 == 0 and maior % numero3 == 0 and maior % numero4 == 0 and maior % numero5 == 0:
            mmc = maior
            break
        else:
            maior += 1

    for i in range(1, maior):
        if numero1 % i == 0 and numero2 % i == 0 and numero3 % i == 0 and numero4 % i == 0 and numero5 % i == 0:
            mdc = i
    print('mmc = {}; mdc = {}'.format(mmc, mdc))
    break