from datetime import date

a = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    n= int(input("Em que ano a {} pessoa nasceu? ".format(pess)))
    i = a - n
    if i >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("Ao todo tivemos {} pessoas maiores de idade".format(totmaior))
print("E também tivemos {} pessoas menores de idade".format(totmenor))
