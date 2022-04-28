nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
média = (nota1 + nota2 + nota3) / 3
print("Tirando {:.1f}, {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(nota1, nota2, nota3, média))

if média >=5 and média < 7:
    print("O aluno está em RECUPERAÇÃO")
elif média < 5:
    print("O aluno está REPROVADO")
elif média >= 7:
    print("O aluno está APROVADO")
