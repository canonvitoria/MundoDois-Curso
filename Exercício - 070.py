total = 0
totmil = 0
menor = 0
cont = 0
barato = 0
while True:
    produto = str(input("Nome do Produto: "))
    preço = float(input("preço: R$"))
    cont += 1
    total += preço
    if preço >1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("{:-^40}".format("FIM DO PROGRAMA"))
print(f"O toral da compra foi {total}")
print(f"Temos {totmil} produtos custando mais de R$1000")
print(f"O produto mais barato foi {barato} que custa R${menor}")