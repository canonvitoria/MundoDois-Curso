'''r = "M, F"
while r == "M, F":
    r = str(input("Informe o seu sexo: [M/F]")).upper()
    if r != r
print("Sexo M resgistrado com sucesso")'''

sexo = str(input("Informe seu sexo: [F/M]")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos. Por faovr, informe seu sexo: ")).strip().upper()
print("Sexo {} resgistrado com sucesso".format(sexo))
