'''while True:
    n = int(input("Gostaria de ver a tabuada de qual valor? "))
    if n < 0:
        break
    print('-' * 30)
    for c in range (1, 11):
        print(f"{n} x {c} = {n * c}")
    print('-' * 30)
print("PROGRAMA DE TABUADA ENCERRADA! Volte sempre!")'''



while True:
    n = int(input("Gostaria de ver a tabuada de qual valor? "))
    print('-' * 30)
    if n < 0:
        break
    for c in range (1, 11):
        print(f"{n} x {c} = {n * c}")
print("O programa de tabuada foi ENCERRADO! Volte sempre!!")






















