nome = str(input("Qual é seu nome? "))
if nome == "Gustavo":  #Condição simples
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem popular no Brasil")
else: #Condição composta
    print("Seu nome é bem normal.")
print("Tenha um bom dia {}".format(nome))