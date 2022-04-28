n = str(input("Digite uma frase: ")).strip().upper()
p = n.split()
j = "".join(p)
i = ""

#Ou inverso = junto[::-1]   macete do fatiamento

for letra in range(len(j) - 1, -1, -1):
    i += j[letra]
print("O inverso {} é {}".format(j, i))
if i == j:
    print("Temos um palídromo!")
else:
    print("Afrase digitada não é um palídromo!")
