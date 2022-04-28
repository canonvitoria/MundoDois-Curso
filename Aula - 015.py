'''cont = 1
while True
    print(cont, '...', end='')
    cont += 1
print("Acabou")'''

'''n = 0
soma = 0
while n != 999:
    n = int(input("Digite um número: "))
    soma += n
soma -= 999
print("A soma vale {}".format(soma))'''

'''n = 0
soma = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    soma += n
#("A soma vale {}".format(soma))
print(f"A soma vale {soma}")'''

#Exemplo com F strings
nome = "José"
idade = 33
print(f"O {nome} tem {idade} anos.")
#antes
print("O {} tem {} anos".format(nome, idade))
