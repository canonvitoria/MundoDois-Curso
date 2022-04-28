resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input("Digite um número: "))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
média = soma / quant
print("Você digitou {} números e a média foi {}".format(quant, média))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))

'''media = 0
qnt = 1
loop = True
maior = 0
menor = 0
soma = 0
while loop == True:
    print('-=-' * 9)
    n = int(input(f'digite o número {qnt}: '))
    c = str(input('quer continuar? [Y/N] ')).upper()
    print('-=-' * 9)

    if c == 'y'.upper():
        print('ok, continue.')
        qnt += 1
    elif c == 'n'.upper():
        loop = False
    else:
        print('\033[1;31mReinicie e digite um valor valido.\033[m')
        break
    media += n

    if n < menor or menor == 0:
        menor = n
    if n > maior or maior == 0:
        maior = n
print(f'A média dos valores é {media / qnt :.1f}')
print(f'O menor número é {menor}.')
print(f'O maior número e {maior}')'''
